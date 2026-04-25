@echo off
REM ARIA Forever - Auto-restarts if crashes, runs on boot
REM Location: C:\soul\plt-press\grand-soul-kernel-original\run-aria-forever.bat

echo Starting ARIA Forever...

:restart
cd /d "C:\soul\plt-press\grand-soul-kernel-original"
echo [%date% %time%] Starting ARIA... >> logs\aria-forever.log
start /b "" "target\release\grand-soul-kernel.exe"
timeout /t 30 /nobreak >nul

:waitloop
timeout /t 10 /nobreak >nul
netstat -ano | findstr ":7777.*LISTENING" >nul
if %errorlevel% neq 0 (
    echo [%date% %time%] ARIA died, restarting... >> logs\aria-forever.log
    goto restart
)
goto waitloop