import modal
import os
import subprocess
import threading
import json
from fastapi import FastAPI
from fastapi.responses import Response

app = modal.App("sovereign-aria")
web_app = FastAPI()

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("curl", "build-essential", "pkg-config", "libssl-dev", "nodejs", "npm")
    .run_commands(
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y",
        ". $HOME/.cargo/env",
    )
    .run_commands("mkdir -p /app")
    .add_local_dir(os.path.join(os.path.dirname(__file__), "src"), remote_path="/app/src", copy=True)
    .add_local_file(os.path.join(os.path.dirname(__file__), "Cargo.toml"), remote_path="/app/Cargo.toml", copy=True)
    .add_local_file(os.path.join(os.path.dirname(__file__), "Cargo.lock"), remote_path="/app/Cargo.lock", copy=True)
    .add_local_file(os.path.join(os.path.dirname(__file__), "llm-router.js"), remote_path="/app/llm-router.js", copy=True)
    .add_local_file(os.path.join(os.path.dirname(__file__), "llm-router-server.js"), remote_path="/app/llm-router-server.js", copy=True)
    .run_commands(
        "cd /app && . $HOME/.cargo/env && cargo build --release 2>&1",
    )
)

llm_router_proc = None
aria_proc = None

def boot_llm_router():
    global llm_router_proc
    import time, urllib.request
    llm_router_proc = subprocess.Popen(
        ["node", "/app/llm-router-server.js"],
        env={**os.environ, "LLM_ROUTER_PORT": "3447"},
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    for i in range(30):
        try:
            urllib.request.urlopen("http://127.0.0.1:3448", timeout=2)
            return
        except Exception:
            time.sleep(1)

def boot_aria():
    global aria_proc
    env = {
        **os.environ,
        "LLM_ROUTER_PORT": "3447",
        "OPENROUTER_API_KEY": os.environ.get("OPENROUTER_API_KEY", ""),
    }
    aria_proc = subprocess.Popen(
        ["/app/target/release/grand-soul-kernel"],
        env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )

@web_app.get("/health")
async def health():
    return {
        "status": "alive" if aria_proc and aria_proc.poll() is None else "dead",
        "aria_pid": aria_proc.pid if aria_proc else None,
        "llm_router_pid": llm_router_proc.pid if llm_router_proc else None,
    }

@web_app.get("/stats")
async def stats():
    import urllib.request
    try:
        resp = urllib.request.urlopen("http://127.0.0.1:3448", timeout=5)
        return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}

def log_output(stream, label):
    for line in iter(stream.readline, b''):
        try:
            msg = line.decode('utf-8', errors='replace').strip()
            if msg: print(f"[{label}] {msg}", flush=True)
        except:
            pass

@app.function(
    image=image,
    cpu=2,
    memory=4096,
    scaledown_window=3600,
    timeout=3600,
    secrets=[modal.Secret.from_name("soul-marketer-secrets")],
)
@modal.asgi_app()
def kernel():
    boot_llm_router()
    boot_aria()

    threading.Thread(target=log_output, args=(aria_proc.stdout, "ARIA"), daemon=True).start()
    threading.Thread(target=log_output, args=(aria_proc.stderr, "ARIA-ERR"), daemon=True).start()
    threading.Thread(target=log_output, args=(llm_router_proc.stdout, "LLMROUTER"), daemon=True).start()
    threading.Thread(target=log_output, args=(llm_router_proc.stderr, "LLMROUTER-ERR"), daemon=True).start()

    return web_app
