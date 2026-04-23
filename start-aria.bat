@echo off
title Aria — Grand Soul Kernel
cd /d "C:\soul\plt-press\grand-soul-kernel-original"
echo Killing old processes...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :7777 ^| findstr LISTENING') do taskkill /PID %%a /F 2>nul
for /f "tokens=1" %%a in ('tasklist ^| findstr grand-soul') do taskkill /IM %%a /F 2>nul
echo Starting Aria...
start "Aria" cmd /k "C:\soul\plt-press\grand-soul-kernel-original\target\release\grand-soul-kernel.exe"
timeout /t 3 /nobreak >nul
start http://localhost:7777/
echo Aria is cycling. Journal should open in your browser.
echo.
echo Say hello: POST a message to Craig at http://localhost:7777/message
echo Or add to craig_messages.json