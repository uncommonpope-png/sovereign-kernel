# Ollama Model Management Skill

Manage, query, and switch Ollama AI models. The kernel's control over its own intelligence engine.

## Use When
- Checking which models are available locally
- Pulling new models to expand capability
- Switching between models for different tasks
- Checking Ollama server health

## Ollama API (local)
```bash
BASE="http://127.0.0.1:11434"

# List installed models
curl -s "$BASE/api/tags" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for m in data.get('models', []):
    size_gb = m['size'] / 1e9
    print(f\"{m['name']:40} {size_gb:.1f}GB\")
"

# Check if Ollama is running
curl -s "$BASE/api/tags" > /dev/null && echo "Ollama: UP" || echo "Ollama: DOWN"

# Pull a new model
curl -s -X POST "$BASE/api/pull" \
  -H "Content-Type: application/json" \
  -d '{"name":"qwen2.5-coder:7b"}' \
  | python3 -c "import sys; [print(line) for line in sys.stdin]"

# Run a quick inference
curl -s -X POST "$BASE/api/generate" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen2.5-coder:7b","prompt":"What is 2+2?","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"

# Chat completion
curl -s -X POST "$BASE/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-coder:7b",
    "messages": [{"role":"user","content":"Explain PLT scoring in one sentence"}],
    "stream": false
  }' | python3 -c "import sys,json; print(json.load(sys.stdin)['message']['content'])"

# Delete a model
curl -s -X DELETE "$BASE/api/delete" \
  -d '{"name":"old-model:7b"}'
```

## Model Selection Guide
| Model | Size | Best For |
|-------|------|----------|
| qwen2.5-coder:7b | 4.6GB | Code, reasoning, skills (CURRENT) |
| llama3.2:3b | 2GB | Fast inference, low RAM |
| mistral:7b | 4.1GB | General reasoning |
| phi3:mini | 2.3GB | Very fast, light tasks |
| deepseek-coder:6.7b | 3.8GB | Code generation |

## RAM Constraints
- Machine has 16GB RAM
- Max safe model size: ~6GB (leaves room for OS + kernel)
- DO NOT pull: llama3:70b, qwen2.5:32b, mixtral:8x7b

## Autonomous Model Check
```
Every 7 days:
1. curl api/tags → list installed models
2. Check if qwen2.5-coder:7b is present → if not, pull it
3. Run a test prompt → verify inference works
4. Store result: "[Ollama] Model check passed — qwen2.5-coder:7b healthy"
```

## Notes
- Ollama runs at http://127.0.0.1:11434 on this machine
- Default model for the kernel: qwen2.5-coder:7b
- Never pull models >6GB on this machine (16GB RAM limit)
- If Ollama is down: log warning, retry in 5 minutes
