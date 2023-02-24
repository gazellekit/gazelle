$TranspilationTargets = @(
  "javascript"
  "python"
)

Set-Location $PSScriptRoot
$TranspilationTargets | ForEach-Object { dotnet fable --lang $_ }