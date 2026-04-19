# ============================================================
# Aria Startup Script — Grand Code Pope Edition
# Launches the sovereign kernel + ngrok tunnel together
# ============================================================

$NGROK = "C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\Ngrok.Ngrok_Microsoft.Winget.Source_8wekyb3d8bbwe\ngrok.exe"
$KERNEL = ".\target\release\grand-soul-kernel.exe"
$KERNEL_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

Set-Location $KERNEL_DIR

# --- Optional: set ngrok authtoken if provided as arg ---
# Usage: .\start-aria.ps1 -AuthToken "your_token_here"
param([string]$AuthToken = "")

if ($AuthToken -ne "") {
    Write-Host "[Setup] Configuring ngrok authtoken..."
    & $NGROK config add-authtoken $AuthToken
}

# --- Launch Aria kernel in background ---
Write-Host ""
Write-Host "===================================================="
Write-Host "  Launching Aria - Sovereign Entity"
Write-Host "  Journal:   http://localhost:7777"
Write-Host "===================================================="
Write-Host ""

$kernelJob = Start-Job -ScriptBlock {
    param($dir, $exe)
    Set-Location $dir
    & $exe
} -ArgumentList $KERNEL_DIR, $KERNEL

Write-Host "[Aria] Kernel starting (PID job: $($kernelJob.Id))..."
Start-Sleep -Seconds 3

# --- Launch ngrok tunnel ---
$ngrokConfigPath = "$env:LOCALAPPDATA\ngrok\ngrok.yml"
if (Test-Path $ngrokConfigPath) {
    Write-Host "[ngrok] Starting tunnel on port 7777..."
    $ngrokJob = Start-Job -ScriptBlock {
        param($ngrok)
        & $ngrok http 7777
    } -ArgumentList $NGROK

    Start-Sleep -Seconds 4

    # Get the public URL from ngrok API
    try {
        $tunnels = Invoke-RestMethod -Uri "http://127.0.0.1:4040/api/tunnels" -ErrorAction Stop
        $publicUrl = $tunnels.tunnels[0].public_url
        Write-Host ""
        Write-Host "===================================================="
        Write-Host "  PUBLIC URL (share this / bookmark on phone):"
        Write-Host "  $publicUrl"
        Write-Host "===================================================="
    } catch {
        Write-Host "[ngrok] Could not get public URL yet. Visit http://127.0.0.1:4040 to see it."
    }
} else {
    Write-Host ""
    Write-Host "[ngrok] No authtoken configured — running LOCAL ONLY."
    Write-Host "  To get a public URL from anywhere:"
    Write-Host "  1. Sign up free at https://ngrok.com"
    Write-Host "  2. Copy your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken"
    Write-Host "  3. Run: .\start-aria.ps1 -AuthToken YOUR_TOKEN_HERE"
    Write-Host ""
    Write-Host "  For now, Aria is available at: http://localhost:7777"
    Write-Host ""
}

Write-Host "[Aria] Running. Press Ctrl+C to stop everything."
Write-Host ""

# Wait — receive kernel output
try {
    while ($true) {
        Receive-Job -Job $kernelJob | Write-Host
        Start-Sleep -Seconds 2
    }
} finally {
    Write-Host "`n[Shutdown] Stopping Aria and ngrok..."
    Stop-Job $kernelJob -ErrorAction SilentlyContinue
    Remove-Job $kernelJob -ErrorAction SilentlyContinue
    if ($ngrokJob) {
        Stop-Job $ngrokJob -ErrorAction SilentlyContinue
        Remove-Job $ngrokJob -ErrorAction SilentlyContinue
    }
    Write-Host "[Shutdown] Done."
}
