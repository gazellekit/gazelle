Set-Location "$PSScriptRoot/.."

$Platforms = @(
  @{ GOOS = "windows"; GOARCH = "amd64" }
  @{ GOOS = "linux"; GOARCH = "amd64" }
  @{ GOOS = "darwin"; GOARCH = "amd64" }
)

$InputFile = "./cmd/gazelle/main.go"

$Platforms | ForEach-Object {
  $Env:GOOS = $_.GOOS
  $Env:GOARCH = $_.GOARCH

  $Extension = if ($_.GOOS -eq "windows") { ".exe" } else { "" }
  $Executable = "gazelle-$($_.GOOS)-$($_.GOARCH)$Extension"
  
  go build -o "./build/$Executable" 
}
