# PowerShell Utilities for Common Tasks.
# Copyright (C) 2023 James S. Bayley
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


using namespace System.IO
using namespace System.Collections.Generic 

# Activate strict mode. 
Set-StrictMode -Version "Latest"

# Errors interrupt script and prevent further execution.
$ErrorActionPreference = "Stop"


function Test-DirectoryPath { 

  <#
    .SYNOPSIS
    Verifies that a given directory path exists on the local machine.

    .DESCRIPTION
    The user must provide the full path to a selected directory on
    the local machine. If the directory is successfully located then 
    the original directory path is returned from the function. In the 
    case that the directory cannot be found, an exception is thrown.

    .INPUTS
    Accepts the directory path via the pipe operator.

    .OUTPUTS
    Returns the provided directory path back to the user if the
    directory is successfully located on the machine. Otherwise, 
    an exception is thrown.

    .PARAMETER Path 
    The full path to the specified directory as a string.

    .EXAMPLE 
    Provide the given path to the function as a string.
    Searching for a directory called "LocalDirectory".

      Test-DirectoryPath -Path "{Root}\Documents\LocalDirectory"
  #>

  [CmdletBinding()]
  param (
    [Parameter(Mandatory, ValueFromPipeline)]
    [ValidateNotNullOrEmpty()]
    [string]$Path 
  )

  process { 
    if (-not [IO.Directory]::Exists($Path)) { 
      throw "Directory not found. Please verify the path."
    }

    return $Path 
  }
}


function Test-FilePath { 

  <#
    .SYNOPSIS
    Verifies that a given file path exists on the local machine.

    .DESCRIPTION
    The user must provide the full path to a selected resource on
    the local machine. If the resource is successfully located then 
    the original file path is returned from the function. In the case
    that the file cannot be found, an exception is thrown.

    .INPUTS
    Accepts the file path string via the pipe operator.

    .OUTPUTS
    Returns the provided file path back to the user if the file 
    is successfully located on the machine. Otherwise, an exception
    is thrown.

    .PARAMETER Path 
    The full path to the specified file as a string.

    .EXAMPLE 
    Pass the given file path to the function as a string.

      Test-FilePath -Path "{Root}\Documents\Test.txt"
  #>

  [CmdletBinding()]
  param (
    [Parameter(Mandatory, ValueFromPipeline)]
    [ValidateNotNullOrEmpty()]
    [string]$Path 
  )

  process { 
    if (-not [IO.File]::exists($Path)) { 
      throw "File not found. Please verify the path."
    }

    return $Path 
  }
}


function Test-FileExtension {

  <#
    .SYNOPSIS
    Verifies that a given file path has the expected extension.

    .DESCRIPTION
    Accepts both a file path and an expected file extension. If
    the file path does not terminate with the given extension 
    then an exception is thrown. Otherwise the original filepath 
    is returned to the caller.
    
    .INPUTS 
    Accepts file path string via the pipe operator.

    .OUTPUTS 
    Returns the original unmodified file path to the caller 
    if the file extension matches the value of the $Extension 
    argument. Otherwise, an exception is thrown.

    .PARAMETER FilePath 
    The file path to validate. 

    .PARAMETER Extension 
    The expected file extension used for pattern matching. 
    Typical extension arguments are .csv, .txt, .json etc.

    .EXAMPLE 
    Check that the provided file path has a .json extension. 
    The function call below will result in an exception being
    thrown.

      Test-FileExtension `
        -FilePath "{Root}/Test.txt" `
        -Extension ".json"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [ValidateNotNullOrEmpty()]
    [string]$FilePath, 

    [Parameter(Mandatory)]
    [ValidatePattern('^(\.)\w+$')]
    [string]$Extension
  )

  process { 
    # Validate path and discard return value.
    $null = Test-FilePath -Path $FilePath

    # Extract the extension as a substring of the path.
    $FilePathExtensionStartIndex = $FilePath.LastIndexOf(".") 
    $FilePathExtension = $FilePath.Substring($FilePathExtensionStartIndex)

    # Validate file path extension.
    if ($FilePathExtension -ne $Extension) { 
      throw "Path $FilePath does not have expected extension: $Extension."
    }

    return $FilePath
  }
}


function Test-FileSize {

  <#
    .SYNOPSIS
    Checks that the file size is within a stated limit.

    .DESCRIPTION
    Compares the size of a specified file against a 
    quoted limit. If the size exceeds the limit then
    an exception is thrown. Otherwise, the original
    file path is returned to the caller.

    .INPUTS
    Accepts a file path via the pipe-operator.

    .OUTPUTS
    Returns the original unmodified file path.

    .PARAMETER FilePath 
    Full path to the file being validated.

    .PARAMETER SizeLimit
    The maximum size file permitted.

    .PARAMETER Units
    The specific file size denomination. This can
    be specified as either KB, MB or GB. 

    .EXAMPLE
    It is assumed that a file is 0.6MB in size. 
    The following function will, therefore, throw 
    an exception as the file size exceeds 0.5MB. 

      Test-FileSize `
        -FilePath $Path `
        -SizeLimit 0.5 `
        -Units "MB"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [string]$FilePath,

    [Parameter(Mandatory)]
    [float]$SizeLimit, 

    [Parameter(Mandatory)]
    [ValidateSet("KB", "MB", "GB")]
    [string]$Units
  )

  process { 
    # Validate file path.
    $null = Test-FilePath -Path $FilePath 

    # Get file size in specified units.
    $Size = (Get-Item -Path $FilePath).Length / "1$Units"

    # Compare file size against chosen limit.
    if ($Size -gt $SizeLimit) { 
      $FileName = Get-FileName -FilePath $FilePath -IncludeFileExtension
      throw "File size of $FileName exceeds $SizeLimit$Units."
    }

    return $FilePath
  }
} 


function Assert-FileIsEmpty { 

  <#
    .SYNOPSIS
    Verifies whether a file at a given path is empty.

    .DESCRIPTION 
    Accepts a file path and checks whether the number of 
    bytes (i.e. the file length) is equal to zero. If so,
    the file is considered empty.

    .INPUTS
    Accepts file path string via the pipe operator.

    .OUTPUTS
    Returns true if the file is empty.

    .PARAMETER Path
    The file path to assess.

    .EXAMPLE 
    Provide a path to a selected file for assertion.
    
      Assert-FileIsEmpty -Path "{Root}/Empty.txt"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [string]$Path
  )

  process { 
    # Verify that path exists and discard result.
    $null = Test-FilePath -Path $Path 

    # If file length is zero, then it is empty.
    return (Get-Item -Path $Path).Length -eq 0
  }
}


function Get-FileName {

  <#
    .SYNOPSIS
    Extracts the file name from a given file path.

    .DESCRIPTION 
    Accepts a file path pointing to a local resource 
    and extracts the name from the string. The caller 
    can also opt to include the file extension with 
    the name via the $IncludeFileExtension flag.

    .INPUTS
    Accepts file path string via the pipe operator.

    .OUTPUTS
    Returns the file name extracted from the file path.

    .PARAMETER FilePath 
    The file path string pointing to a local resource.

    .PARAMETER IncludeFileExtension
    Optional flag to include the file extension.

    .EXAMPLE 
    Return the name "ExampleFile.txt" from the path.

      Get-FileName `
        -Path "{Root}/Desktop/ExampleFile.txt" `
        -IncludeFileExtension
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [string]$FilePath, 

    [Parameter()]
    [switch]$IncludeFileExtension
  )

  process { 
    # Verify that path exists and discard result.
    $null = Test-FilePath -Path $FilePath 

    # Extract file name from path.
    if ($IncludeFileExtension) {
      return [IO.Path]::GetFileName($FilePath)
    }
    else { 
      return [IO.Path]::GetFileNameWithoutExtension($FilePath)
    }
  }
}


function Read-JsonFile { 

  <#
    .SYNOPSIS
    Reads the contents of a JSON file into memory. 

    .DESCRIPTION
    Accepts a path to a local .json file and attempts to parse the 
    contents into memory. If parsing is successful, the file is 
    converted to a PSCustomObject and returned to the caller. 

    .INPUTS
    Function does not support piped input.

    .OUTPUTS
    Returns the parsed JSON file contents as a PSCustomObject.

    .PARAMETER Path
    The JSON file path.

    .EXAMPLE 
    Provide path to the relevant .json file and return the contents.

      Read-JsonFile -Path "{Root}/config.json"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$Path 
  )

  process { 
    # Validate path and discard return value.
    $null = Test-FilePath -Path $Path 
    $null = Test-FileExtension -FilePath $Path -Extension ".json"

    # Attempt to parse JSON.
    return (Get-Content $Path | ConvertFrom-Json)  
  }

  end { 
    Write-Host "Loaded JSON file: $($Path.Split([Path]::DirectorySeparatorChar)[-1])."
  }
}


function Read-TsvFile { 

  <#
    .SYNOPSIS
    Attempts to parse a given .tsv file into memory as a PSCustomObject. 

    .DESCRIPTION
    Accepts a file path for a selected .tsv file and parses the contents
    into an in-memory data structure. The .tsv file can be split into
    either rows or columns. The caller can opt to skip the first row of 
    a .tsv file to avoid parsing column headers. 

    .INPUTS
    Function does not support piped input.

    .OUTPUTS
    Returns the parsed .tsv file contents as a PSCustomObject.

    .PARAMETER Path 
    The Tab-Separated Values (TSV) file path.

    .PARAMETER SplitBy
    Allows the caller to split the .tsv file contents either by row or column. 

    .PARAMETER SkipFirstLine 
    Optional flag allowing the caller to skip the first row of the .tsv file, 
    which typically contains column headers that may not be relevant for 
    data post-processing. The parameter defaults to $false.

    .EXAMPLE 
    Split given .tsv file by column and skip first row containing the headers.

      Read-TsvFile `
        -Path "{Root}/data.tsv"
        -SplitBy "Column"
        -SkipFirstLine $true
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$Path,

    [Parameter(Mandatory)]
    [ValidateSet("Column", "Row")]
    [string]$SplitBy,

    [Parameter()]
    [bool]$SkipFirstLine = $false
  )

  process { 
    # Verify file path and discard return value.
    $null = Test-FilePath -Path $Path
    $null = Test-FileExtension -FilePath $Path -Extension ".tsv"

    # If file is empty, return null.
    if ((Assert-FileIsEmpty -Path $Path) -eq $true) { 
      return $null
    } 

    # Instantiate reader and optionally skip first line (e.g. headers).
    $Reader = [IO.StreamReader]::new($Path)

    if ($SkipFirstLine -eq $true) { 
      $null = $Reader.ReadLine()

      # If there is no content following
      # the first line, then return null.
      if ($Reader.Peek() -eq -1) { 
        return $null
      }
    }

    # Parse file contents.
    switch ($SplitBy) { 
      "Row" {
        # Initialise List<string[]>.
        $Rows = [List[string[]]]::new()

        # Lazily evaluate and split each subsequent line in the
        # file and append the values onto the respective rows.
        while ($null -ne ($Line = $Reader.ReadLine())) { 
          $Rows.Add($Line.Split("`t"))
        }

        return $Rows
      }

      "Column" { 
        # Read and split the first line only.
        $FirstLineValues = $Reader.ReadLine().Split("`t")

        # Count non-empty columns.
        $NumberOfColumns = ($FirstLineValues | 
          Where-Object { -not [String]::IsNullOrWhiteSpace($_) } |
          Measure-Object).Count

        # Initialise column array.
        $Columns = @(0) * $NumberOfColumns

        # Initialise List<string> for each element in the 
        # column array and append the first row values onto
        # the respective columns.
        for ($i = 0; $i -lt $NumberOfColumns; $i++) { 
          $Columns[$i] = [List[string]]::new() 
          $Columns[$i].Add($FirstLineValues[$i])
        }

        # Lazily evaluate and split each line in the file
        # and append the values onto the respective columns.
        while ($null -ne ($Line = $Reader.ReadLine())) {
          $Values = $Line.Split("`t")
          for ($i = 0; $i -lt $NumberOfColumns; $i++) { 
            $Columns[$i].Add($Values[$i])
          }
        }

        return $Columns
      }
    }
  }

  end { 
    Write-Host "Loaded TSV file: $($Path.Split(""\"")[-1])"
  }
}


function Convert-TsvFileToJson {

  <#
    .SYNOPSIS
    Parses a .tsv file before converting its content to JSON.
    
    .DESCRIPTION
    Accepts a .tsv file path and parses its contents into local
    memory. After parsing, a JSON property name is computed by
    extracting the filename from the provided path. Finally,
    each data column is extracted as a nested JSON property and 
    the column heading is used as the nested property name.  
    
    .INPUTS
    The function accepts file path strings via the pipe operator.

    .OUTPUTS 
    Returns a JSON object containing the .tsv file name as a key 
    and the parsed file contents as the associated value.

    .PARAMETER Path
    The Tab-Separated Values (TSV) file path. 

    .EXAMPLE 
    Pipe multiple .tsv file paths into the function producing a JSON object 
    consisting of keys for each file name mapped against the respective 
    file's contents.

      @(
        "{Root}/data1.txt",
        "{Root}/data2.txt"
      ) | Convert-TsvFileToJson
  #>

  [CmdletBinding()]
  param (
    [Parameter(Mandatory, ValueFromPipeline)]
    [ValidateNotNullOrEmpty()]
    [string]$Path    
  )

  begin { 
    Write-Host "`nConverting TSV file(s) to JSON..." -ForegroundColor "Yellow"
    $Hashtable = [ordered]@{}
  }

  process { 
    # Compute hashtable key to map against file contents.
    $Key = Get-FileName -FilePath $Path

    # Add .tsv file name to hashtable and initialise nested map.
    $Hashtable[$Key] = [ordered]@{}

    # Parse .tsv file into memory.
    $Data = Read-TsvFile `
      -Path $Path `
      -SplitBy "Column"

    # Map .tsv file to hashtable using column headers as hash keys.
    for ($i = 0; $i -lt $Data.Length; $i++) {
      $Column = $Data[$i]
      $Title = $Column[0]
      $NumberOfValues = $Column.Count - 1
      switch ($NumberOfValues) {
        0 {
          $Hashtable[$Key][$Title] = @()
        }
        default {
          $Values = $Column[1..$NumberOfValues]
          $Hashtable[$Key][$Title] = $Values
        }
      }
    }
  }

  end { 
    Write-Host "TSV file(s) successfully converted to JSON.`n" -ForegroundColor "Green"
    $Json = ConvertTo-Json -InputObject $Hashtable
    return $Json
  }
}


function Add-TsvDataToHashtable {

  <#
    .SYNOPSIS
    Parses a .tsv file before adding its contents to a hashtable.
    
    .DESCRIPTION
    Accepts a .tsv file path and parses its contents into local
    memory. The TSV data can be split either by row or column to
    suit the caller's requirements. After parsing, a key name 
    is computed by extracting the filename from the provided 
    path. The key and file contents are added to a hashtable.

    .INPUTS
    The function accepts file path strings via the pipe operator.

    .OUTPUTS 
    Returns a hashtable containing the .tsv file name as a key 
    and the parsed file contents as the associated value.

    .PARAMETER Path
    The Tab-Separated Values (TSV) file path.

    .PARAMETER SplitBy
    Allows the caller to split the .tsv file contents either by row or column. 

    .PARAMETER SkipFirstLine 
    Optional flag allowing the caller to skip the first row of the .tsv file, 
    which typically contains column headers that may not be relevant for 
    data post-processing. The parameter defaults to $false.

    .EXAMPLE 
    Pipe multiple .tsv file paths into the function producing a hashtable 
    consisting of keys for each file name mapped against the respective 
    file's contents. In this example, the header row is included for each 
    file and the data is split by row ($SkipFirstLine defaults to $false).

      @(
        "{Root}/data1.txt",
        "{Root}/data2.txt"
      ) | Add-TsvDataToHashtable -SplitBy "Row" 
  #>

  [CmdletBinding()]
  param (
    [Parameter(Mandatory, ValueFromPipeline)]
    [ValidateNotNullOrEmpty()]
    [string]$Path,
    
    [Parameter(Mandatory)]
    [ValidateSet("Column", "Row")]
    [string]$SplitBy,

    [Parameter()]
    [bool]$SkipFirstLine = $false    
  )

  begin { 
    Write-Host "`nAdding TSV file(s) to hashtable..." -ForegroundColor "Yellow"
    $Hashtable = @{}
  }
  
  process { 
    # Compute hashtable key to map against file contents.
    $Key = Get-FileName -FilePath $Path

    # Parse .tsv file into memory.
    $Data = Read-TsvFile `
      -Path $Path `
      -SplitBy $SplitBy `
      -SkipFirstLine $SkipFirstLine

    # Add .tsv file contents to hashtable.
    $Hashtable[$Key] = $Data
  }

  end { 
    Write-Host "TSV files successully loaded.`n" -ForegroundColor "Green"
    return $Hashtable
  }
}


function Remove-WhiteSpace { 

  <#
    .SYNOPSIS
    Strips whitespace from a given string.

    .DESCRIPTION
    Carries out Regular Expression whitespace replacement. 

    .INPUTS
    Accepts string via the pipe-operator.

    .OUTPUTS
    Returns the original string without whitespace.

    .PARAMETER Text
    The string to strip of whitespace.

    .EXAMPLE
    The following string has its whitespace removed
    and returns "NoMoreWhiteSpace".

      Remove-WhiteSpace `
        -Text "No More White Space"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [AllowEmptyString()]
    [string]$text
  )

  process { 
    return ($text -replace '\s+', "")
  }
}
