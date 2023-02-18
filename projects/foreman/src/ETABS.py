import sys
import comtypes.client

from enum import IntEnum
from typing import Self


class ETABS:

  """
  Class.
  """

  class Version(IntEnum):
    20

  def __init__(self, version: Version) -> Self: 
    self.version = version
    self.ETABS_API = None
    self.SAP_API = None 


  def start(self) -> Self:
    """
    Startup Module.
    """

    try:
       self.ETABS_API = _get_ETABS_API_object(self.version)
    except (OSError, comtypes.COMError):
      print("Cannot start a new instance of the program.")
      sys.exit(-1)


    self.ETABS_API.ApplicationStart()
    self.SAP_API = self.ETABS_API.SapModel
    self.SAP_API.InitializeNewModel()

    return self


def _get_ETABS_API_object(version: ETABS.Version):

    def get_v1_helper():
      return comtypes \
        .client \
        .CreateObject("ETABSv1.Helper") \
        .QueryInterface(comtypes.gen.ETABSv1.cHelper) \
        .CreateObjectProgID("CSI.ETABS.API.ETABSObject")

    return { 
      20: get_v1_helper()
    }[version]

    