Set-Location "$PSScriptRoot/.."

$DirectoryCommands = @(
  @{ RelativePath = "."; Command = "npm install -g npm" }
  @{ RelativePath = "./projects"; Command = "dotnet tool restore" }
  @{ RelativePath = "projects/structures"; Command = "npm install" }
  @{ RelativePath = "projects/fortress"; Command = "npm install" }
) 

$DirectoryCommands | ForEach-Object { 
  Push-Location $_.RelativePath
  Invoke-Expression $_.Command
  Pop-Location
}
