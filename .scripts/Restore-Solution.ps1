Set-Location "$PSScriptRoot/.."

$DirectoryCommands = @(
  @{ RelativePath = "."; Command = "npm install -g npm" }
  @{ RelativePath = "."; Command = "dotnet tool restore" }
  @{ RelativePath = "."; Command = "dotnet restore" }
  @{ RelativePath = "src/Calcpad.Studio.Core"; Command = "npm install" }
) 

$DirectoryCommands | ForEach-Object { 
  Push-Location $_.RelativePath
  Invoke-Expression $_.Command
  Pop-Location
}
