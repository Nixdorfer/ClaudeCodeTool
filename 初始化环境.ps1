$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=== 初始化CC工具包环境 ===" -ForegroundColor Cyan
Write-Host ""

$mcpDir = Join-Path $PSScriptRoot "mcp\code-RAG"
Set-Location $mcpDir

Write-Host "[1/2] 创建venv..."
python -m venv venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "[错误] 无法创建venv 请确保你安装了Python 3.11+" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[2/2] 正在安装依赖..."
& "$mcpDir\venv\Scripts\Activate.ps1"
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "[错误] 无法安装依赖" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "环境安装完成" -ForegroundColor Green
Read-Host "Press Enter to exit"