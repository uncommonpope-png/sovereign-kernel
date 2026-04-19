# Encryption & Secrets Skill

Manage secrets, API keys, and encrypted data. Keep sensitive information safe.

## Use When
- Storing API keys securely (not in plaintext files)
- Encrypting sensitive data before writing to disk
- Generating secrets, tokens, and passwords
- Validating that secrets are properly set

## Environment Variables (preferred for secrets)
```bash
# Check if secret is set
[[ -z "$OPENAI_API_KEY" ]] && echo "WARNING: OPENAI_API_KEY not set" || echo "OK"

# Load from .env file
set -a; source .env; set +a

# Windows PowerShell
if (-not $env:OPENAI_API_KEY) { Write-Warning "OPENAI_API_KEY not set" }
$env:OPENAI_API_KEY = Get-Content .env | Select-String "OPENAI_API_KEY=(.+)" | ForEach-Object {$_.Matches.Groups[1].Value}
```

## .env File Format
```
# C:\soul\plt-press\grand-soul-kernel-original\.env
OPENAI_API_KEY=sk-...
BRAVE_API_KEY=BSA...
GITHUB_TOKEN=ghp_...
OLLAMA_HOST=http://127.0.0.1:11434
PLT_KERNEL_SECRET=...
```

## Generate Secure Tokens
```python
import secrets, hashlib

# Random API token
token = secrets.token_urlsafe(32)
print(f"Token: {token}")

# Random hex
key = secrets.token_hex(16)
print(f"Key: {key}")

# Hash a secret (for storage comparison)
import hashlib
hashed = hashlib.sha256("my_secret".encode()).hexdigest()
print(f"Hash: {hashed}")
```

## Encrypt/Decrypt Data (Fernet symmetric)
```python
# pip install cryptography
from cryptography.fernet import Fernet

# Generate key (store safely!)
key = Fernet.generate_key()
print(f"Key: {key.decode()}")  # Save to secure location

# Encrypt
f = Fernet(key)
encrypted = f.encrypt(b"sensitive data here")
print(f"Encrypted: {encrypted[:40]}...")

# Decrypt
decrypted = f.decrypt(encrypted)
print(f"Decrypted: {decrypted.decode()}")
```

## Kernel Secrets Pattern
```
1. Store API keys in .env file (add .env to .gitignore!)
2. Load at startup: read .env into environment
3. Never log secret values — log "API_KEY: [set]" not the value
4. Rotate secrets: generate new token, update .env, test, delete old
5. When pushing to GitHub: ensure .gitignore includes .env, *.key, *.pem
```

## .gitignore for Secrets
```
.env
*.key
*.pem
*.p12
secrets/
entity_state.json    # may contain sensitive memory
```

## Notes
- NEVER hardcode secrets in main.rs or any source file
- NEVER commit .env to git
- Use environment variables for runtime secrets
- For production: use a proper secrets manager (1Password, AWS Secrets Manager)
