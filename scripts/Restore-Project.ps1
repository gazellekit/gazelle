Set-Location $PSScriptRoot/..

$DirectoryCommands = @(
  @{ RelativePath = "projects"; Command = "dotnet tool restore" }
  @{ RelativePath = "projects/Fortress"; Command = "dotnet restore" },
  @{ RelativePath = "projects/Fortress.Tests"; Command = "dotnet restore" }
) 

$DirectoryCommands | ForEach-Object { 
  Push-Location $_.RelativePath
  Invoke-Expression $_.Command
  Pop-Location
}
