$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=== code-RAG Setup ===" -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot

Write-Host "[1/2] Creating venv..."
python -m venv venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to create venv. Ensure Python 3.11+ is installed." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[2/2] Installing dependencies..."
& "$PSScriptRoot\venv\Scripts\Activate.ps1"
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Done! Add .mcp.json to your project root to activate code-RAG." -ForegroundColor Green
Read-Host "Press Enter to exit"
