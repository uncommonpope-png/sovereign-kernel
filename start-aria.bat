@echo off
REM ARIA Kernel Startup Script

cd /d "C:\soul\plt-press\grand-soul-kernel-original"

echo Starting ARIA (Queen)...
start /b target\release\grand-soul-kernel.exe

REM Wait for port 7777
timeout /t 3 /nobreak >nul

REM Verify
netstat -ano | findstr ":7777.*LISTENING" >nul
if %errorlevel% neq 0 (
    echo ERROR: ARIA failed to start
    exit /b 1
)

echo ARIA running on port 7777
echo   - /healthz health check
echo   - /keys/status API keys
echo   - /chat history
exit /b 0