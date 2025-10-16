@echo off
title Zipwn Launcher
color 3

REM Change to script directory (same folder as this batch file)
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH!
    pause
    exit
)

REM Check if script exists
if not exist "WinRAR-Cracker.py" (
    echo WinRAR-Cracker.py not found!
    echo Looking in: %CD%
    pause
    exit
)

REM Run the Python script
python WinRAR-Cracker.py

pause