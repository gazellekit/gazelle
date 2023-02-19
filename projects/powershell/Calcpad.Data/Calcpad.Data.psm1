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

# Activate strict mode. 
Set-StrictMode -Version "Latest"

# Errors interrupt script and prevent further execution.
$ErrorActionPreference = "Stop"

# Error codes for common errors:
#   0 -> Null, empty or whitespace.
#   1 -> Character limit exceeded.
#   2 -> N/A, TBC, or TBA.
#   3 -> Regex failure.


function Assert-NonEmptyString { 

  <#
    .SYNOPSIS
    Validates that a given string contains content
    and does not exceed a predefined character limit.

    .DESCRIPTION
    Accepts a string and runs a series of validation 
    checks to verify that the value is neither null,
    empty, whitespace, or of length greater than a 
    predefined limit, or equal to N/A, TBC or TBA 
    (case-insensitive).

    .INPUTS
    Accepts string value via pipe-operator.

    .OUTPUTS
    Returns an error string, alongside a defined error 
    code, in the case that a given validation function 
    fails. Otherwise, returns true.

    .PARAMETER Value
    The string to validate.

    .EXAMPLE
    The following string returns true.

      Assert-NonEmptyString -Value "This is valid!"

    .EXAMPLE
    The following function call will return "Invalid 
    value: N/A, TBC or TBA".

      Assert-NonEmptyString -Value "n/a"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [AllowEmptyString()]
    [string]$Value
  )

  process { 
    $Regex = '^(n/a|tbc|tba)$'

    if ([string]::IsNullOrWhiteSpace($Value)) { 
      return ("String is null, empty or whitespace.", 0)
    }
    elseif ($Value.Length -gt 2000) { 
      return ("String exceeds 2000 character limit.", 1)
    }
    elseif ($Value -match $Regex) { 
      return ("String is N/A, TBC or TBA.", 2)
    }
    else { 
      return $true
    }
  }
}


function Assert-ValidEmailAddress { 

  <# 
    .SYNOPSIS
    Validates the format of a given email address.

    .DESCRIPTION
    Carries out null, whitespace, length and regex 
    validation checks on a given email address.

    .INPUTS
    Accepts an email address via the pipe-operator.

    .OUTPUTS
    Returns an error string, alongside a defined error 
    code, if a validation check fails. Otherwise, 
    returns true.

    .PARAMETER EmailAddress
    The email address string to validate.

    .EXAMPLE
    The following email address is not formatted in
    accordance with the requisite regex pattern and 
    therefore returns an error string. 

      Assert-ValidEmailAddress `
        -EmailAddress "john.doe@gmail"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [AllowEmptyString()]
    [string]$EmailAddress
  )

  process { 
    $NARegex = '^(n/a|tbc|tba)$'
    $EmailRegex = '^\w[\.\w]*\w@\w[\-\w]*\.([a-z]|[a-z]\.[a-z])+\s*$'

    if ([string]::IsNullOrWhiteSpace($EmailAddress)) { 
      return ("Email address is null, empty or whitespace.", 0)
    }
    elseif ($EmailAddress.Length -gt 254) { 
      return ("Email address exceeds 254 character limit.", 1)
    }
    elseif ($EmailAddress -match $NARegex) { 
      return ("Email address is N/A, TBC or TBA.", 2)
    }
    elseif ($EmailAddress -notmatch $EmailRegex) { 
      return ("Email address format is invalid.", 3)
    }
    else { 
      return $true
    }
  }
}


function Assert-ValidPhoneNumber { 
  
  <#
    .SYNOPSIS
    Validates the format of a given phone number.

    .DESCRIPTION
    Strips whitespace before carrying out null, 
    whitespace, length and regex validation checks 
    on a given phone number.

    .INPUTS
    Accepts a phone number via the pipe-operator.

    .OUTPUTS
    Returns an error string, alongside a defined error 
    code, if a validation check fails. Otherwise, 
    returns true.

    .PARAMETER PhoneNumber
    The phone number string to validate.

    .EXAMPLE
    The following phone number is not formatted in
    accordance with the requisite regex pattern and 
    therefore returns an error string. 

      Assert-ValidPhoneNumber `
        -PhoneNumber "+(32)120"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [AllowEmptyString()]
    [string]$PhoneNumber
  )

  process { 
    $NARegex = '^(n/a|tbc|tba)$'
    $PhoneRegex = '^(\d{11}|\(\+\d{2}\)\d{10,11}|\+\d{2}\(0\)\d{10}|\+\d{2}\d{10})$'
    
    $PhoneNumber = Remove-WhiteSpace -Text $PhoneNumber

    if ([string]::IsNullOrWhiteSpace($PhoneNumber)) { 
      return ("Phone number is null, empty or whitespace.", 0)
    }
    elseif ($PhoneNumber.Length -gt 16) { 
      return ("Phone number exceeds 16 characters.", 1)
    }
    elseif ($PhoneNumber -match $NARegex) { 
      return ("Phone number is N/A, TBC or TBA.", 2)
    }
    elseif ($PhoneNumber -notmatch $PhoneRegex) { 
      return ("Phone number format is invalid.", 3)
    }
    else { 
      return $true
    }
  }
}


function Assert-ValidDateTime { 

  <#
    .SYNOPSIS
    Validates the format of a given datetime.

    .DESCRIPTION
    Strips whitespace before carrying out null, 
    whitespace, length and regex validation checks 
    on a given datetime string.

    .INPUTS
    Accepts a datetime string via the pipe-operator.

    .OUTPUTS
    Returns an error string, alongside a defined error 
    code, if a validation check fails. Otherwise, 
    returns true.

    .PARAMETER DateTime
    The datetime string string to validate.

    .EXAMPLE
    The following datetime is not formatted in
    accordance with the requisite regex pattern 
    because it contains a W between the date 
    and time components instead of a T. An
    error string is returned. 

      Assert-ValidDateTime `
        -DateTime "2021-02-12W18:56:54"
  #>

  [CmdletBinding()]
  param(
    [Parameter(Mandatory, ValueFromPipeline)]
    [AllowEmptyString()]
    [string]$DateTime
  )

  process { 
    $NARegex = '^(n/a|tbc|tba)$'
    $DateTimeRegex = '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'

    $DateTime = Remove-WhiteSpace -Text $DateTime

    if ([string]::IsNullOrWhiteSpace($DateTime)) { 
      return ("DateTime is null, empty or whitespace.", 0)
    }
    elseif ($DateTime.Length -gt 19) { 
      return ("DateTime exceeds 19 characters.", 1)
    }
    elseif ($DateTime -match $NARegex) { 
      return ("DateTime is N/A, TBC or TBA.", 2)
    }
    elseif ($DateTime -notmatch $DateTimeRegex) { 
      return ("DateTime format is invalid.", 3)
    }
    else { 
      return $true
    }
  }
}
