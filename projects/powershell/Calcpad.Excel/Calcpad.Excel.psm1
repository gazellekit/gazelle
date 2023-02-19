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


using namespace System 
using namespace System.IO

# Import module dependencies.
Import-Module FileManager

# Activate Strict Mode.
Set-StrictMode -Version "Latest"

# Errors interrupt script and prevent further execution.
$ErrorActionPreference = "Stop"


function Split-ExcelWorkbook {

  <# 
    .SYNOPSIS 
    Splits an excel workbook into individual sheets (.csv/.tsv).

    .DESCRIPTION
    A workbook is split into its constituent worksheets and
    saved as either .csv or .tsv. The user can opt to pipe-in 
    paths to multiple Excel files; each workbook is then 
    decomposed into a separate unique sub-directory. 

    .INPUTS 
    Accepts multiple Excel workbook file paths via the pipe operator.

    .OUTPUTS
    Decomposes the original workbook(s) into a series of individual
    worksheets that are grouped together into a single unique directory.
    If multiple file paths were piped in, then the decomposed sheets
    from each respective Excel file are stored separately as a group. 
    I.e., if 3 file paths are input, then 3 output directories will 
    be produced: one for each corresponding Excel file. The path to 
    the newly created directory containing the split worksheets is 
    returned to the caller.

    .PARAMETER OutputFileType
    The user must specify the desired output file type for 
    the individually saved worksheets. The supported file 
    types are comma-separated values (csv) and tab-separated
    values (tsv). Acceptable arguments are either csv or tsv.

    .PARAMETER ExcelFilePath 
    The full path to the referenced Excel file, including the .xlsx 
    extension. If multiple paths are piped into the script then each 
    file is located and split independently.

    .PARAMETER OutputDirectoryPath 
    An optional parameter enabling the user to specify a 
    different output directory for the decomposed worksheets. 
    By default, a directory containing the individual sheets
    is deployed onto the user desktop. 

    .EXAMPLE 
    Split an Excel workbook into separate .csv files and 
    place in default directory on the user desktop.

    Split-ExcelWorkbook `
      -OutputFileType "csv" `
      -ExcelFilePath "{fullpath}\Example.xlsx"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory)]
    [ValidateSet("csv", "tsv")]
    [string]$OutputFileType,

    [Parameter(Mandatory, ValueFromPipeline)]
    [string]$ExcelFilePath,

    [Parameter()]
    [string]$OutputDirectoryPath = [Environment]::GetFolderPath("desktop")
  )

  begin { 
    # Verify that all instances of Excel are closed because 
    # the 'end' block will terminate every active Excel process.
    Write-Warning "Ensure all active Excel workbooks are closed prior to start."
    $Proceed = Read-Host -Prompt "Proceed [Y/n]?"
    if (-not ($Proceed -eq "Y")) { 
      throw "User aborted script execution."
    }

    # Progress notification.
    Write-Host "`nConnecting to Excel..." -ForegroundColor "Yellow"

    # Attempt to launch headless Excel.
    try {
      $Excel = New-Object -ComObject "Excel.Application"
      $Excel.Visible = $false 
      $Excel.DisplayAlerts = $false 
    }
    catch {
      Write-Error "Failed to launch Excel: $($_.Exception.Message)."
    }
  }

  process { 
    # 1. Check that file path has .xlsx extension.
    $null = Test-FileExtension -FilePath $ExcelFilePath -Extension ".xlsx"

    # 2. Check Excel file exists.
    $null = Test-FilePath -Path $ExcelFilePath

    # 3. Check that specified output directory exists.
    $null = Test-DirectoryPath -Path $OutputDirectoryPath

    # 4. Open specified workbook.
    $Workbook = $Excel.Workbooks.Open($ExcelFilePath)

    # 5. Create directory at output path (incl. postfix if path already exists). 
    $ExcelFileName = Get-FileName -FilePath $ExcelFilePath
    $COBieSheetsDirectoryPath = "$OutputDirectoryPath/$ExcelFileName"

    if ([IO.Directory]::Exists($COBieSheetsDirectoryPath)) { 
      $DirectoryExists = $true
      $Postfix = 0

      while ($DirectoryExists) { 
        $Postfix += 1
        $DirectoryExists = [IO.Directory]::Exists("$COBieSheetsDirectoryPath-$Postfix")
      }

      $COBieSheetsDirectoryPath += "-$Postfix"
    }

    try { 
      $null = [IO.Directory]::CreateDirectory("$COBieSheetsDirectoryPath")
    }
    catch { 
      Write-Error "Failed to create directory: $($_.Exception.Message)."
    }
    
    # 6. Save all worksheets to the output directory and monitor completion.
    Write-Host "Exporting worksheets."

    $SheetCount = 0
    $TotalNumberOfSheets = $Workbook.Worksheets.Count 

    $FileFormatCode = switch ($OutputFileType) {
      "csv" { 6 }
      "tsv" { 20 }
    }

    foreach ($Worksheet in $Workbook.Worksheets) {
      $FileName = "$($Worksheet.Name)"
      $SavePath = "$COBieSheetsDirectoryPath/$FileName.$OutputFileType"

      try { 
        $null = $Worksheet.SaveAs($SavePath, $FileFormatCode)
      }
      catch {
        Write-Error "Failed to save $($FileName): $($_.Exception.Message)."
      }
      
      $SheetCount += 1
      Write-Host "$SheetCount/$TotalNumberOfSheets sheets saved."
    }

    # 7. Close the active workbook.
    $null = $Workbook.Close($false)

    # 8. Process complete.
    Write-Host "`n$SheetCount file(s) saved successfully." -ForegroundColor "Green"

    # 9. Return worksheets directory path.
    return $COBieSheetsDirectoryPath
  }

  end { 
    # Clean up system resources.
    $null = $Excel.Quit()
    Stop-Process -ProcessName "EXCEL"
  }
}
