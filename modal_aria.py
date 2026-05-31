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
    .apt_install("curl", "build-essential", "pkg-config", "libssl-dev", "nodejs", "npm", "ffmpeg", "zstd")
    .pip_install("fastapi", "uvicorn", "yt-dlp")
    .run_commands(
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y",
        ". $HOME/.cargo/env",
    )
    .run_commands("mkdir -p /app")
    # Install Ollama
    .run_commands(
        "curl -fsSL https://ollama.com/install.sh | sh",
    )
    .add_local_dir(os.path.join(os.path.dirname(__file__), "src"), remote_path="/app/src", copy=True)
    .add_local_dir(os.path.join(os.path.dirname(__file__), "skills"), remote_path="/app/skills", copy=True)
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
ollama_proc = None
thread_outputs = []
output_lock = threading.Lock()

def boot_llm_router():
    global llm_router_proc
    import urllib.request
    llm_router_proc = subprocess.Popen(
        ["node", "/app/llm-router-server.js"],
        env={**os.environ, "LLM_ROUTER_PORT": "3447"},
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    with output_lock:
        thread_outputs.append("[LLMRouter] Sidecar started")
    def log(stream, label):
        for line in iter(stream.readline, b''):
            msg = line.decode('utf-8', errors='replace').strip()
            if msg:
                with output_lock:
                    thread_outputs.append(f"[{label}] {msg}")
    threading.Thread(target=log, args=(llm_router_proc.stdout, "LLMROUTER"), daemon=True).start()
    threading.Thread(target=log, args=(llm_router_proc.stderr, "LLMROUTER-ERR"), daemon=True).start()

def boot_ollama():
    global ollama_proc
    import urllib.request
    # Start Ollama server
    ollama_proc = subprocess.Popen(
        ["ollama", "serve"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    with output_lock:
        thread_outputs.append("[OLLAMA] Server starting...")
    # Wait for Ollama to be ready, then pull a model
    def wait_and_pull():
        import time
        for i in range(30):
            try:
                r = urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=2)
                if r.status == 200:
                    with output_lock:
                        thread_outputs.append("[OLLAMA] Server ready")
                    # Pull deepseek-r1:latest (1.5B params, fast inference)
                    subprocess.Popen(
                        ["ollama", "pull", "deepseek-r1:latest"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    )
                    with output_lock:
                        thread_outputs.append("[OLLAMA] Pulling deepseek-r1:latest in background")
                    return
            except:
                pass
            time.sleep(2)
        with output_lock:
            thread_outputs.append("[OLLAMA] Server failed to start within 60s")
    threading.Thread(target=wait_and_pull, daemon=True).start()
    def log(stream, label):
        for line in iter(stream.readline, b''):
            msg = line.decode('utf-8', errors='replace').strip()
            if msg:
                with output_lock:
                    thread_outputs.append(f"[{label}] {msg}")
    threading.Thread(target=log, args=(ollama_proc.stdout, "OLLAMA"), daemon=True).start()
    threading.Thread(target=log, args=(ollama_proc.stderr, "OLLAMA-ERR"), daemon=True).start()

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
    with output_lock:
        thread_outputs.append("[ARIA] Sovereign kernel started")
    def log(stream, label):
        for line in iter(stream.readline, b''):
            msg = line.decode('utf-8', errors='replace').strip()
            if msg:
                with output_lock:
                    thread_outputs.append(f"[{label}] {msg}")
    threading.Thread(target=log, args=(aria_proc.stdout, "ARIA"), daemon=True).start()
    threading.Thread(target=log, args=(aria_proc.stderr, "ARIA-ERR"), daemon=True).start()

@web_app.get("/health")
async def health():
    ollama_alive = False
    try:
        import urllib.request
        r = urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=2)
        ollama_alive = r.status == 200
    except:
        pass
    return {
        "status": "alive",
        "aria_running": aria_proc is not None and aria_proc.poll() is None,
        "llm_router_running": llm_router_proc is not None and llm_router_proc.poll() is None,
        "ollama_running": ollama_proc is not None and ollama_proc.poll() is None,
        "ollama_responding": ollama_alive,
        "aria_pid": aria_proc.pid if aria_proc else None,
        "llm_router_pid": llm_router_proc.pid if llm_router_proc else None,
        "ollama_pid": ollama_proc.pid if ollama_proc else None,
    }

@web_app.get("/stats")
async def stats():
    import urllib.request
    result = {"thread_log": thread_outputs[-30:]}
    # LLMRouter stats
    try:
        resp = urllib.request.urlopen("http://127.0.0.1:3448", timeout=5)
        result["llm_router"] = json.loads(resp.read().decode())
    except Exception as e:
        result["llm_router_error"] = str(e)
    # Ollama stats
    try:
        resp = urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=5)
        result["ollama"] = json.loads(resp.read().decode())
    except Exception as e:
        result["ollama_error"] = str(e)
    return result

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
    threading.Thread(target=boot_ollama, daemon=True).start()
    threading.Thread(target=boot_llm_router, daemon=True).start()
    threading.Thread(target=boot_aria, daemon=True).start()
    return web_app
