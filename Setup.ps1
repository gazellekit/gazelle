Set-Location $PSScriptRoot

$DirectoryCommands = @(
  @{ RelativePath = "."; Command = "sudo dotnet workload update" }
  @{ RelativePath = "."; Command = "dotnet tool restore" }
  @{ RelativePath = "."; Command = "dotnet tool install --global PowerShell" }
  @{ RelativePath = "."; Command = "dotnet restore" }
) 

$DirectoryCommands | ForEach-Object { 
  Push-Location $_.RelativePath
  Invoke-Expression $_.Command
  Pop-Location
}