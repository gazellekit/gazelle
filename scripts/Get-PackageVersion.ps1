Set-Location "$PSScriptRoot/.."
Push-Location "projects/Fortress"
(Get-Content "global.config" | ConvertFrom-Json).version
Pop-Location