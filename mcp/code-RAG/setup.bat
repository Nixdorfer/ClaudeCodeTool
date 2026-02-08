@echo off
chcp 65001 > nul
echo === code-RAG Setup ===
echo.

cd /d "%~dp0"

echo [1/2] Creating venv...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create venv. Ensure Python 3.11+ is installed.
    pause
    exit /b 1
)

echo [2/2] Installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)

echo.
echo Done! Add .mcp.json to your project root to activate code-RAG.
pause
