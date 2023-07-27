Set-Location "$PSScriptRoot/.."

$DirectoryCommands = @(
  @{ RelativePath = "."; Command = "npm install -g npm" }
  @{ RelativePath = "./projects"; Command = "dotnet tool restore" }
  @{ RelativePath = "./projects/Calcpad.Studio.Core"; Command = "npm install" }
) 

$DirectoryCommands | ForEach-Object { 
  Push-Location $_.RelativePath
  Invoke-Expression $_.Command
  Pop-Location
}
