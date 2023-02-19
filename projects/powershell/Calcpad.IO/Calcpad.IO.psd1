@{
    # Script module or binary module file associated with this manifest.
    RootModule        = './Calcpad.IO.psm1'

    # Version number of this module.
    ModuleVersion     = '0.0.1'

    # ID used to uniquely identify this module
    GUID              = '9f5a023b-fc59-4369-b250-f662926603b6'

    # Author of this module
    Author            = 'James Bayley'

    # Description of the functionality provided by this module
    Description       = 'File and Path utilities.'

    # Functions to export from this module, for best performance, do not use wildcards and do not delete the entry, use an empty array if there are no functions to export.
    FunctionsToExport = @(
        "Test-DirectoryPath",
        "Test-FilePath", 
        "Test-FileSize",
        "Test-FileExtension", 
        "Assert-FileIsEmpty",
        "Get-FileName",
        "Read-JsonFile",
        "Read-TsvFile",
        "Add-TsvDataToHashtable",
        "Convert-TsvFileToJson",
        "Remove-WhiteSpace"
    )
}

