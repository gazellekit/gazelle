# Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Setup PowerShell Profile](#setup-powershell-profile)
  - [Configure PowerShell Module Path](#configure-powershell-module-path)
  - [Exploring Available Functions](#exploring-available-functions)
  - [Using Help Docs](#using-help-docs)
- [Updating PowerShell Modules](#updating-powershell-modules)

# Overview

Calcpad is a collection of convenient utilities that run in PowerShell 7.X. 

# Getting Started

## Setup PowerShell Profile

Typically, for convenience and practicality, developers like to have direct access to the modules from their top-level PowerShell environment, so that they can call specific functions from whenever they like without having to navigate to the precise file location. One of the simplest ways to accomplish this task with PowerShell is to create a 'profile'. 

1. To check if you already have a PowerShell profile, run the following command from any location within your terminal prompt: 

```powershell

Test-Path $profile.CurrentUserAllHosts

```

2. If the function returns `true`, then you already have the correctly scoped profile and can skip to step 3. Otherwise, run the following command to create your profile: 

```powershell

New-Item $profile.CurrentUserAllHosts -Type file -Force

```

3. Open the profile in Notepad: 

```powershell

notepad $profile.CurrentUserAllHosts

```

## Configure PowerShell Module Path

It's important to understand that when PowerShell instances start-up, they scan a series of pre-defined directories for available modules. 

1. To see which directories PowerShell searches through, run the following command: 

```powershell

$Env:PSModulePath.Split(";")

```

You'll notice that the returned list contains a handful of PowerShell Module directories that are searched by default. Whilst we could have theoretically placed our own Calcpad modules in one of these pre-defined locations, I find it safer and more convenient to simply add a new search path to `$Env:PSModulePath` so that we do not have to interfere with the existing directory structures. 

2. Copy the full path to the previously cloned `Calcpad` directory and then within your open notepad file add the following line (__note__ the required semicolon `;` at the beginning of the path): 

```powershell

$Env:PSModulePath += ";Path/To/Calcpad/Directory"

```

3.  Save the notepad file and close it.

4.  Close your existing terminal window and start a fresh instance. This is because the `$profile.CurrentUserAllHosts` file is read once when the terminal first launches. Any changes to the file whilst the terminal is active are _not_ automatically captured. Launching a fresh instance allows PowerShell to reload all profiles.

5.  That's it! You should now be setup. To check whether your modules have been successfully mapped, simply run the command below. You should see the `Calcpad` modules listed at the end.

```powershell

Get-Module -ListAvailable

```

## Exploring Available Functions

1. To see the full list of available functions within a module, run the following command: 

```powershell

Get-Command -Module Calcpad.IO

```

## Using Help Docs

1.  For inline help documentation about a function, run the command below. In this instance we are requesting documentation regarding the `Test-DirectoryPath` function from the `Calcpad.IO` module. 

```powershell

Get-Help Test-DirectoryPath 

```

2. To see worked examples for a given function, add the `-Examples` flag to the previous command. Again, we will use the `Test-DirectoryPath` function as an example.

```powershell

Get-Help Test-DirectoryPath -Examples 

```

# Updating PowerShell Modules

Once you've worked through the [Getting Started](#getting-started) steps above, capturing any module updates should be trivial. Simply navigate to the cloned `Calcpad` directory in your terminal and run the following command:

```powershell

git pull

```

That's all there is to it. 

Just remember the following two points: 

1. You should relaunch your PowerShell terminal after capturing the updates.
2. If you change the path/location of the `Calcpad` directory on your machine, you will need to return to the [Configure PowerShell Module Path](#configure-powershell-module-path) step to correct your `$Env:PSModulePath` with the modified folder location.
