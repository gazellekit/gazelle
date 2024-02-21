class SteelSectionCategoryNotFound(BaseException):
    """
    A specified steel section category is either
    currently unsupported in our application, or
    simply does not exist in the Blue Book data.
    """


class SteelSectionDesignationNotFound(BaseException):
    """
    A specified steel section designation is
    either currently unsupported in our application,
    or simply does not exist in the Blue Book data.
    """


class SteelFabricatorNotSupported(BaseException):
    """
    The specified steel fabricator either is either 
    currently unsupported in our application, or 
    simply does not exist.
    """
