Set-Location "$PSScriptRoot/.."

$DirectoryCommands = @(
  @{ RelativePath = "."; Command = "npm install -g npm" }
  @{ RelativePath = "projects"; Command = "dotnet tool restore" }
  @{ RelativePath = "projects"; Command = "dotnet restore" }
  @{ RelativePath = "projects/fortress/src"; Command = "npm install" }
) 

$DirectoryCommands | ForEach-Object { 
  Push-Location $_.RelativePath
  Invoke-Expression $_.Command
  Pop-Location
}
