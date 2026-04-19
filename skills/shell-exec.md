# Shell Execution Skill

Run shell commands, scripts, and system operations. The kernel's voice in the operating system.

## Use When
- Running any system command or script
- Executing build tools (cargo, npm, python)
- Automating OS-level tasks
- Checking system state

## Run Commands (Windows PowerShell)
```powershell
# Run command and capture output
$result = & cmd /c "dir C:\soul"
$result

# Run with timeout
$job = Start-Job { cargo build }
Wait-Job $job -Timeout 120
Receive-Job $job

# Run Python script
python3 script.py arg1 arg2

# Run cargo
$env:PATH = "C:\msys64\mingw64\bin;" + $env:PATH
cargo build 2>&1
cargo check 2>&1
cargo run 2>&1

# Check exit code
& some-command; echo "Exit: $LASTEXITCODE"
```

## Run Commands (Unix/Linux)
```bash
# Simple execution
bash -c "command here"

# With timeout
timeout 30 bash -c "long-running command"

# Background process
nohup python3 script.py &

# Capture stdout and stderr
output=$(command 2>&1)

# Check if command exists
which cargo && echo "cargo found" || echo "cargo not found"
```

## Script Execution Pattern
```
1. Write script to temp file
2. Set execute permission (Unix: chmod +x)
3. Run with timeout
4. Capture exit code and output
5. Log result as episodic memory
6. Delete temp file when done
```

## Build & Run Kernel
```powershell
# Full build
$env:PATH = "C:\msys64\mingw64\bin;" + $env:PATH
Set-Location C:\soul\plt-press\grand-soul-kernel-original
cargo build 2>&1

# Quick check only
cargo check 2>&1
```

## System Info
```bash
# CPU/memory
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
# or: top -bn1 (Linux)

# Disk space
Get-PSDrive C | Select-Object Used, Free
# or: df -h (Linux)

# Running processes
Get-Process | Where-Object {$_.Name -like "*rust*"}
```

## Notes
- Always capture stderr (2>&1) for build tools
- Use timeouts for any external commands — never hang
- Log all executed commands and their exit codes
- On Windows: use PowerShell. On Unix: use bash
