@{

    # Script module or binary module file associated with this manifest.
    RootModule        = './Calcpad.Data.psm1'

    # Version number of this module.
    ModuleVersion     = '0.0.1'

    # ID used to uniquely identify this module
    GUID              = '973f14f2-1707-4f2e-806c-9880d4584add'

    # Author of this module
    Author            = 'James Bayley'

    # Description of the functionality provided by this module
    Description       = 'Data validation and transformation utilities.'

    # Functions to export from this module, for best performance, do not use wildcards and do not delete the entry, use an empty array if there are no functions to export.
    FunctionsToExport = @(
        'Assert-NonEmptyString',
        'Assert-ValidEmailAddress',
        'Assert-ValidPhoneNumber',
        'Assert-ValidDateTime'       
    )
}

