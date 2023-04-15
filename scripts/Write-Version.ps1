Set-Location "$PSScriptRoot/../projects/Fortress"

$PackageVersion = (Get-Content "global.config" | ConvertFrom-Json).version

@("Fortress.fsproj", "package.json") | ForEach-Object { 
  (Get-Content $_).Replace("{{ VERSION }}", $PackageVersion) | Set-Content $_
}