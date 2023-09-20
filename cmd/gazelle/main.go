package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/calcpadstudio/gazelle/internal/core"
)

func main() {
	fmt.Println("Gazelle 🦌 A fast, cross-platform CLI for Structural Analysis & Design.")
	fmt.Println("Press Enter to continue...")
	bufio.NewReader(os.Stdin).ReadBytes('\n')
	fmt.Println("You are using", core.LibraryName)
}
