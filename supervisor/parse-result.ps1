param(
    [Parameter(Mandatory=$true)]
    [string]$TaskId,

    [string]$ProjectSlug = "",

    [int]$MaxChars = 2000,

    [switch]$Full
)

$tempBase = "$env:LOCALAPPDATA\Temp\claude"

function Resolve-OutputFile {
    if ($ProjectSlug -ne "") {
        $f = Join-Path $tempBase $ProjectSlug "tasks" "$TaskId.output"
        if (Test-Path $f) { return $f }
    }
    $dirs = Get-ChildItem $tempBase -Directory
    foreach ($d in $dirs) {
        $f = Join-Path $d.FullName "tasks" "$TaskId.output"
        if (Test-Path $f) { return $f }
    }
    return $null
}

$outputFile = Resolve-OutputFile
if (-not $outputFile) {
    Write-Host "Output file not found for task $TaskId" -ForegroundColor Red
    exit 1
}

$lines = Get-Content $outputFile -ErrorAction SilentlyContinue
if (-not $lines) {
    Write-Host "Empty output file" -ForegroundColor Yellow
    exit 0
}

$textBlocks = @()
$toolCalls = @()
$errors = @()
$fileEdits = @()

foreach ($line in $lines) {
    try {
        $obj = $line | ConvertFrom-Json -ErrorAction Stop
    } catch { continue }

    if ($obj.type -ne "assistant" -or -not $obj.message) { continue }
    if (-not $obj.message.content) { continue }

    foreach ($block in $obj.message.content) {
        if ($block.type -eq "text" -and $block.text) {
            $textBlocks += $block.text
        }
        if ($block.type -eq "tool_use") {
            $toolCalls += "$($block.name)($($block.input | ConvertTo-Json -Compress -Depth 1))"

            if ($block.name -in @("Write", "Edit")) {
                if ($block.input.file_path) {
                    $fileEdits += $block.input.file_path
                }
            }
        }
    }
}

foreach ($line in $lines) {
    try {
        $obj = $line | ConvertFrom-Json -ErrorAction Stop
    } catch { continue }

    if ($obj.type -eq "user" -and $obj.message -and $obj.message.content) {
        foreach ($block in $obj.message.content) {
            if ($block.type -eq "tool_result" -and $block.is_error) {
                $errText = if ($block.content.Length -gt 100) { $block.content.Substring(0, 100) + "..." } else { $block.content }
                $errors += $errText
            }
        }
    }
}

Write-Host "SUMMARY" -ForegroundColor Cyan
Write-Host "  Tool calls: $($toolCalls.Count)" -ForegroundColor White
Write-Host "  Text blocks: $($textBlocks.Count)" -ForegroundColor White
Write-Host "  Errors: $($errors.Count)" -ForegroundColor $(if ($errors.Count -gt 0) { "Red" } else { "Green" })

if ($fileEdits.Count -gt 0) {
    $uniqueFiles = $fileEdits | Sort-Object -Unique
    Write-Host "  Files modified: $($uniqueFiles.Count)" -ForegroundColor Yellow
    foreach ($f in $uniqueFiles) {
        $short = $f -replace '.*\\(packages|crates|apps)\\', '$1\'
        Write-Host "    - $short" -ForegroundColor DarkYellow
    }
}

if ($errors.Count -gt 0) {
    Write-Host "`nERRORS:" -ForegroundColor Red
    foreach ($e in $errors) {
        Write-Host "  ! $e" -ForegroundColor Red
    }
}

if ($textBlocks.Count -gt 0) {
    Write-Host "`nFINAL OUTPUT:" -ForegroundColor Green
    $lastText = $textBlocks[-1]
    if (-not $Full -and $lastText.Length -gt $MaxChars) {
        Write-Host $lastText.Substring(0, $MaxChars) -ForegroundColor White
        Write-Host "... (truncated, use -Full to see all)" -ForegroundColor DarkGray
    } else {
        Write-Host $lastText -ForegroundColor White
    }
}
