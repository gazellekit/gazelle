#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

GOOS=windows GOARCH=amd64 go build \
  -o $SCRIPT_DIR/../build/gazelle-windows-amd64.exe \
  $SCRIPT_DIR/../cmd/gazelle/main.go

GOOS=linux GOARCH=amd64 go build \
  -o $SCRIPT_DIR/../build/gazelle-linux-amd64 \
  $SCRIPT_DIR/../cmd/gazelle/main.go

GOOS=darwin GOARCH=amd64 go build \
  -o $SCRIPT_DIR/../build/gazelle-darwin-amd64 \
  $SCRIPT_DIR/../cmd/gazelle/main.go