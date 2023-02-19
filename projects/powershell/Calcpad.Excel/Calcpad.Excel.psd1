@{
    # Script module or binary module file associated with this manifest.
    RootModule        = './Calcpad.Excel.psm1'

    # Version number of this module.
    ModuleVersion     = '0.0.1'

    # ID used to uniquely identify this module
    GUID              = 'c43839ed-706b-476f-b5ad-49484bac71e9'

    # Author of this module
    Author            = 'James Bayley'

    # Description of the functionality provided by this module
    Description       = 'Microsoft Excel utilities.'

    # Functions to export from this module, for best performance, do not use wildcards and do not delete the entry, use an empty array if there are no functions to export.
    FunctionsToExport = @("Split-ExcelWorkbook")
}

