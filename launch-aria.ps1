# Aria Launcher - loads keys from Windows user environment variables
# Keys must be set via: [System.Environment]::SetEnvironmentVariable("KEY_NAME", "value", "User")
$env:OPENROUTER_API_KEY = [System.Environment]::GetEnvironmentVariable("OPENROUTER_API_KEY", "User")
$env:HUGGINGFACE_API_KEY = [System.Environment]::GetEnvironmentVariable("HUGGINGFACE_API_KEY", "User") 
$env:GROQ_API_KEY = [System.Environment]::GetEnvironmentVariable("GROQ_API_KEY", "User")
$env:GEMINI_API_KEY = [System.Environment]::GetEnvironmentVariable("GEMINI_API_KEY", "User")
$env:MISTRAL_API_KEY = [System.Environment]::GetEnvironmentVariable("MISTRAL_API_KEY", "User")
$env:GITHUB_COPILOT_TOKEN = [System.Environment]::GetEnvironmentVariable("GITHUB_COPILOT_TOKEN", "User")

Set-Location 'C:\soul\plt-press\grand-soul-kernel-original'
& '.\target\release\grand-soul-kernel.exe'