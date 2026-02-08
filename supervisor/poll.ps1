param(
    [Parameter(Mandatory=$true)]
    [string[]]$TaskIds,
    [int]$TimeoutSeconds = 600
)

$tempBase = "$env:LOCALAPPDATA\Temp\claude"

function Find-TaskDir {
    $dirs = Get-ChildItem $tempBase -Directory -ErrorAction SilentlyContinue
    foreach ($d in $dirs) {
        $tasksDir = Join-Path $d.FullName "tasks"
        foreach ($id in $TaskIds) {
            if (Test-Path (Join-Path $tasksDir "$id.output")) {
                return $tasksDir
            }
        }
    }
    return $null
}

function Test-AgentDone($file) {
    $raw = Get-Content $file -Raw -ErrorAction SilentlyContinue
    if (-not $raw) { return $false }
    if ($raw -match '"stop_reason"\s*:\s*"end_turn"') { return $true }
    if ($raw -match '"type"\s*:\s*"result"') { return $true }
    return $false
}

function Get-AgentErrors($file) {
    $lines = Get-Content $file -ErrorAction SilentlyContinue
    $errs = @()
    foreach ($line in $lines) {
        try {
            $obj = $line | ConvertFrom-Json -ErrorAction Stop
            if ($obj.type -eq "user" -and $obj.message -and $obj.message.content) {
                foreach ($block in $obj.message.content) {
                    if ($block.type -eq "tool_result" -and $block.is_error) {
                        $errs += $block.content.Substring(0, [Math]::Min(150, $block.content.Length))
                    }
                }
            }
        } catch { continue }
    }
    return $errs
}

$taskDir = $null
$waited = 0
while (-not $taskDir -and $waited -lt 30) {
    $taskDir = Find-TaskDir
    if (-not $taskDir) { Start-Sleep -Seconds 1; $waited++ }
}
if (-not $taskDir) {
    Write-Output "ERROR: task dir not found after 30s"
    exit 1
}

$startTime = Get-Date

while ($true) {
    $elapsed = ((Get-Date) - $startTime).TotalSeconds
    if ($elapsed -ge $TimeoutSeconds) {
        $pending = ($TaskIds | Where-Object { -not (Test-AgentDone (Join-Path $taskDir "$_.output")) }) -join ","
        Write-Output "TIMEOUT|pending=$pending"
        exit 2
    }

    $allDone = $true
    foreach ($id in $TaskIds) {
        $file = Join-Path $taskDir "$id.output"
        if (-not (Test-Path $file) -or -not (Test-AgentDone $file)) {
            $allDone = $false
            break
        }
    }

    if ($allDone) {
        $results = @()
        $hasError = $false
        foreach ($id in $TaskIds) {
            $file = Join-Path $taskDir "$id.output"
            $errs = Get-AgentErrors $file
            if ($errs.Count -gt 0) {
                $hasError = $true
                $results += "FAIL|$id|$($errs.Count) errors|$($errs[0])"
            } else {
                $results += "OK|$id"
            }
        }
        Write-Output "DONE"
        foreach ($r in $results) { Write-Output $r }
        if ($hasError) { exit 1 } else { exit 0 }
    }

    Start-Sleep -Seconds 1
}
