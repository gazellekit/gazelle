Set-Location "$PSScriptRoot/.."

$DirectoryCommands = @(
  @{ RelativePath = "."; Command = "npm install -g npm" }
  @{ RelativePath = "./projects"; Command = "dotnet tool restore" }
) 

$DirectoryCommands | ForEach-Object { 
  Push-Location $_.RelativePath
  Invoke-Expression $_.Command
  Pop-Location
}
