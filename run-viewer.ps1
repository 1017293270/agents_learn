$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$port = 8765

Set-Location -LiteralPath $root
Write-Host "Serving knowledge viewer:"
Write-Host "http://127.0.0.1:$port/viewer/"
Write-Host ""
Write-Host "Press Ctrl+C to stop."

python -m http.server $port --bind 127.0.0.1

