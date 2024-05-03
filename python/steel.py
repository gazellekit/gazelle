# SPDX-License-Identifier: AGPL-3.0-or-later
# Gazelle: A fast, open-source engine for civil engineers.
# Copyright (C) 2024 James S. Bayley

"""
The Steel for Life 'Blue Book' is the standard tome used by Structural Engineers
in the UK to design and specify structural steel sections. The book contains
a plethora of design data that is fundamental to steel design in accordance with
Eurocode 3 (EC3). This module provides a convenient API interface to interact
with, and transform, the data captured within the Blue Book. Data has been
sourced from the official website: https://www.steelforlifebluebook.co.uk.
"""

import json
import pathlib
from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, NewType, Tuple, TypeVar, Union

from .units import (
  Area,
  Carbon,
  Centimetre,
  Kilogram,
  Mass,
  Metre,
  Millimetre,
  SurfaceArea,
  Tonne,
)

SectionDesignation = NewType("SectionDesignation", str)
SectionProperties = NewType("SectionProperties", dict[str, Union[bool, float]])


class SectionCategory(Enum):
  UB = "Universal Beam"
  UC = "Universal Column"
  PFC = "Parallel Flange Channel"
  UBP = "Universal Bearing Pile"
  EQUAL_L = "Equal L Section"
  UNEQUAL_L = "Unequal L Section"
  COLD_FORMED_CHS = "Cold Formed Circular Hollow Section"
  COLD_FORMED_RHS = "Cold Formed Rectangular Hollow Section"
  COLD_FORMED_SHS = "Cold Formed Square Hollow Section"
  HOT_FORMED_CHS = "Hot Formed Circular Hollow Section"
  HOT_FORMED_RHS = "Hot Formed Rectangular Hollow Section"
  HOT_FORMED_SHS = "Hot Formed Square Hollow Section"
  HOT_FORMED_EHS = "Hot Formed Elliptical Hollow Section"
  T_SPLIT_FROM_UB = "T Split From UB Section"
  T_SPLIT_FROM_UC = "T Split From UC Section"


class SteelSectionCategoryNotFound(BaseException):
  """
  A specified steel section category is either currently unsupported in our
  application, or simply does not exist in the Blue Book data.
  """


class SteelSectionDesignationNotFound(BaseException):
  """
  A specified steel section designation is either currently unsupported in
  our application, or simply does not exist in the Blue Book data.
  """


class SteelFabricatorNotSupported(BaseException):
  """
  The specified steel fabricator either is either currently unsupported in our
  application, or simply does not exist.
  """


class SteelSection(ABC):
  """
  Abstract base class representations common to all steel sections.

  Typically, users will not use this module directly. All 'concrete' steel
  sections implemented elsewhere within the package inherit from classes within
  this module. Users can reliably depend on the attributes and methods defined
  herein as the public interface for all steel sections and collections of steel
  sections.

  Nevertheless, specific steel section types do provide more specialised,
  refined implementations and additional attributes. Therefore, if a particular
  attribute has not been defined within the abstract base classes, it is worth
  checking the specific section implementations.

  The real advantage of this module is that it provides generic behaviours that
  are common to all steel sections, regardless of their specific geometries.
  For example, all steel sections have a 'mass per metre length', hence it is
  sensible to capture this behaviour at the top of the class hierarchy.
  """

  def __init__(self, des: SectionDesignation, props: SectionProperties, length: Metre):
    """Initialise the section."""
    self._properties = props
    self.designation = des
    self.length = length

  @property
  def is_nonstandard(self) -> bool:
    """Whether the section is non-standard (i.e., uncommon in the UK)."""
    return self._properties["Is Non-Standard"]

  @property
  def cross_sectional_area(self) -> Area[Centimetre]:
    """The cross-sectional area of the section."""
    return Area(self._properties["Area of Section, A (cm2)"], Centimetre)

  @property
  def total_mass(self) -> Kilogram:
    """The total mass of the section."""
    return self.mass_per_metre_length * self.length

  @property
  def mass_per_metre_length(self) -> Mass.PerUnitLength[Kilogram, Metre]:
    """The mass per metre length of the section."""
    return Kilogram(self._properties["Mass Per Metre (kg/m)"]).per_unit_length(Metre)

  @property
  def surface_area_per_metre(self) -> SurfaceArea.PerUnitLength[Metre, Metre]:
    """The surface area per metre length of the section."""
    return SurfaceArea(
      self._properties["Surface Area Per Metre (m2)"], Metre
    ).per_unit_length(Metre)

  @property
  def surface_area_per_tonne(self) -> SurfaceArea.PerUnitMass[Metre, Tonne]:
    """The surface area per tonne of the section."""
    return SurfaceArea(
      self._properties["Surface Area Per Tonne (m2)"], Metre
    ).per_unit_mass(Tonne)

  @property
  def carbon_per_metre(self) -> Carbon.PerUnitLength[Metre]:
    """The carbon per metre length of the section."""
    return Carbon(self._properties["Carbon Per Metre (CO2/m)"]).per_unit_length(Metre)

  def to_json(self):
    """Return a JSON representation of the section."""
    return {
      "sectionClassification": str(self),
      "isNonstandard": self.is_nonstandard,
      "sectionProperties": {
        "length": self.length.to_json(),
        "massPerMetreLength": self.mass_per_metre_length.to_json(),
        "totalMass": self.total_mass.to_json(),
        "crossSectionalArea": self.cross_sectional_area.to_json(),
        "surfaceAreaPerMetre": self.surface_area_per_metre.to_json(),
        "surfaceAreaPerTonne": self.surface_area_per_tonne.to_json(),
        # "carbonPerMetre": self.carbon_per_metre.to_json()
      },
    }

  @abstractmethod
  def __str__(self) -> str:
    pass


S = TypeVar("S", bound=SteelSection)


class SteelSections(Generic[S]):
  """A collection of steel sections."""

  def __init__(self, sections: list[S]):
    """Initialise the collection."""
    self.sections = sections

  def __len__(self):
    """Return the number of sections in the collection."""
    return len(self.sections)

  def __getitem__(self, index: int):
    """Return the section at the given index."""
    return self.sections[index]

  def to_json(self):
    """Return a JSON representation of the collection."""
    return {section.designation: section.to_json() for section in self.sections}


class UniversalSection(SteelSection, ABC):
  @property
  def depth(self) -> Millimetre:
    return Millimetre(self._properties["Depth of Section, h (mm)"])

  @property
  def width(self) -> Millimetre:
    return Millimetre(self._properties["Width of Section, b (mm)"])

  @property
  def web_thickness(self) -> Millimetre:
    return Millimetre(self._properties["Web Thickness, tw (mm)"])

  @property
  def flange_thickness(self) -> Millimetre:
    return Millimetre(self._properties["Flange Thickness, tf (mm)"])

  @property
  def root_radius(self) -> Millimetre:
    return Millimetre(self._properties["Root Radius, r (mm)"])

  @property
  def depth_between_fillets(self) -> Millimetre:
    return Millimetre(self._properties["Depth Between Fillets, d (mm)"])

  @property
  def end_clearance_for_detailing(self) -> Millimetre:
    return Millimetre(self._properties["End Clearance Dimension for Detailing, C (mm)"])

  @property
  def long_notch_dimension(self) -> Millimetre:
    return Millimetre(self._properties["Longitudinal Notch Dimension, N (mm)"])

  @property
  def vertical_notch_dimension(self) -> Millimetre:
    return Millimetre(self._properties["Vertical Notch Dimension, n (mm)"])

  @property
  def radius_of_gyration_yy(self) -> Centimetre:
    return Centimetre(self._properties["Radius of Gyration, Y-Y (cm)"])

  @property
  def radius_of_gyration_zz(self) -> Centimetre:
    return Centimetre(self._properties["Radius of Gyration, Z-Z (cm)"])

  def to_json(self):
    return {
      "sectionClassification": str(self),
      "isNonstandard": self.is_nonstandard,
      "sectionProperties": {
        "length": self.length.to_json(),
        "massPerMetreLength": self.mass_per_metre_length.to_json(),
        "totalMass": self.total_mass.to_json(),
        "crossSectionalArea": self.cross_sectional_area.to_json(),
        "surfaceAreaPerMetre": self.surface_area_per_metre.to_json(),
        "surfaceAreaPerTonne": self.surface_area_per_tonne.to_json(),
        "carbonPerMetre": self.carbon_per_metre.to_json(),
        "depth": self.depth.to_json(),
        "width": self.width.to_json(),
        "webThickness": self.web_thickness.to_json(),
        "flangeThickness": self.flange_thickness.to_json(),
        "rootRadius": self.root_radius.to_json(),
        "depthBetweenFillets": self.depth_between_fillets.to_json(),
        "endClearanceForDetailing": self.end_clearance_for_detailing.to_json(),
        "longitudinalNotchDimension": self.long_notch_dimension.to_json(),
        "verticalNotchDimension": self.vertical_notch_dimension.to_json(),
        "radiusOfGyration": {
          "yy": self.radius_of_gyration_yy.to_json(),
          "zz": self.radius_of_gyration_zz.to_json(),
        },
      },
    }

  @abstractmethod
  def __str__(self):
    pass


class RectangularHollowSection(SteelSection, ABC):
  """A rectangular hollow section."""

  @property
  def width(self) -> Millimetre:
    """The width of the section."""
    return Millimetre(self.designation.split("x")[0])

  @property
  def depth(self) -> Millimetre:
    """The depth of the section."""
    return Millimetre(self.designation.split("x")[1])

  @property
  def flange_thickness(self) -> Millimetre:
    """The thickness of each vertical flange."""
    return Millimetre(self.designation.split("x")[2])

  @property
  def web_thickness(self) -> Millimetre:
    """The thickness of each horizontal web."""
    return Millimetre(self.designation.split("x")[2])

  def to_json(self):
    """Return a JSON representation of the section."""
    return {
      "sectionClassification": str(self),
      "isNonstandard": self.is_nonstandard,
      "sectionProperties": {
        "width": self.width.to_json(),
        "depth": self.depth.to_json(),
        "length": self.length.to_json(),
        "massPerMetreLength": self.mass_per_metre_length.to_json(),
        "totalMass": self.total_mass.to_json(),
        "crossSectionalArea": self.cross_sectional_area.to_json(),
        "surfaceAreaPerMetre": self.surface_area_per_metre.to_json(),
        "surfaceAreaPerTonne": self.surface_area_per_tonne.to_json(),
        "carbonPerMetre": self.carbon_per_metre.to_json(),
        "flangeThickness": self.flange_thickness.to_json(),
        "webThickness": self.web_thickness.to_json(),
      },
    }

  @abstractmethod
  def __str__(self):
    pass


class EllipticalHollowSection(SteelSection, ABC):
  """An elliptical hollow section."""

  @property
  def width(self) -> Millimetre:
    """The width of the section."""
    return Millimetre(self.designation.split("x")[0])

  @property
  def depth(self) -> Millimetre:
    """The depth of the section."""
    return Millimetre(self.designation.split("x")[1])

  @property
  def plate_thickness(self) -> Millimetre:
    """The thickness of each vertical flange."""
    return Millimetre(self.designation.split("x")[1])

  def to_json(self):
    """Return a JSON representation of the section."""
    return {
      "sectionClassification": str(self),
      "isNonstandard": self.is_nonstandard,
      "sectionProperties": {
        "width": self.width.to_json(),
        "depth": self.depth.to_json(),
        "length": self.length.to_json(),
        "massPerMetreLength": self.mass_per_metre_length.to_json(),
        "totalMass": self.total_mass.to_json(),
        "crossSectionalArea": self.cross_sectional_area.to_json(),
        "surfaceAreaPerMetre": self.surface_area_per_metre.to_json(),
        "surfaceAreaPerTonne": self.surface_area_per_tonne.to_json(),
        "carbonPerMetre": self.carbon_per_metre.to_json(),
        "plateThickness": self.plate_thickness.to_json(),
      },
    }

  @abstractmethod
  def __str__(self):
    pass


class CircularHollowSection(SteelSection, ABC):
  """A circular hollow section."""

  @property
  def diameter(self) -> Millimetre:
    """The width of the section."""
    return Millimetre(self.designation.split("x")[0])

  @property
  def plate_thickness(self) -> Millimetre:
    """The thickness of each vertical flange."""
    return Millimetre(self.designation.split("x")[1])

  def to_json(self):
    """Return a JSON representation of the section."""
    return {
      "sectionClassification": str(self),
      "isNonstandard": self.is_nonstandard,
      "sectionProperties": {
        "length": self.length.to_json(),
        "diameter": self.diameter.to_json(),
        "massPerMetreLength": self.mass_per_metre_length.to_json(),
        "totalMass": self.total_mass.to_json(),
        "crossSectionalArea": self.cross_sectional_area.to_json(),
        "surfaceAreaPerMetre": self.surface_area_per_metre.to_json(),
        "surfaceAreaPerTonne": self.surface_area_per_tonne.to_json(),
        "carbonPerMetre": self.carbon_per_metre.to_json(),
        "plateThickness": self.plate_thickness.to_json(),
      },
    }

  @abstractmethod
  def __str__(self):
    pass


class UniversalBeam(UniversalSection):
  def __str__(self):
    return f"Universal Beam (UB) Section: {self.designation}"


class UniversalColumn(UniversalSection):
  def __str__(self):
    return f"Universal Column (UC) Section: {self.designation}"


class UniversalBearingPile(UniversalSection):
  def __str__(self):
    return f"Universal Bearing Pile (UBP) Section: {self.designation}"


class HotFormedRectangularHollowSection(RectangularHollowSection):
  """A hot-formed rectangular hollow section."""

  def __str__(self):
    return f"Hot Formed Rectangular Hollow Section (HF-RHS): {self.designation}"


class ColdFormedRectangularHollowSection(RectangularHollowSection):
  """A cold-formed rectangular hollow section."""

  def __str__(self):
    return f"Cold Formed Rectangular Hollow Section (CF-RHS): {self.designation}"


class HotFormedSquareHollowSection(RectangularHollowSection):
  """A hot-formed square hollow section."""

  def __str__(self):
    return f"Hot Formed Square Hollow Section (HF-SHS): {self.designation}"


class ColdFormedSquareHollowSection(RectangularHollowSection):
  """A cold-formed square hollow section."""

  def __str__(self):
    return f"Cold Formed Square Hollow Section (CF-SHS): {self.designation}"


class HotFormedCircularHollowSection(CircularHollowSection):
  """A hot-formed circular hollow section."""

  def __str__(self):
    return f"Hot Formed Circular Hollow Section (HF-CHS): {self.designation}"


class ColdFormedCircularHollowSection(CircularHollowSection):
  """A cold-formed circular hollow section."""

  def __str__(self):
    return f"Cold Formed Circular Hollow Section (CF-CHS): {self.designation}"


class HotFormedEllipticalHollowSection(EllipticalHollowSection):
  """A hot-formed elliptical hollow section."""

  def __str__(self):
    return f"Hot Formed Elliptical Hollow Section (HF-EHS): {self.designation}"


class SteelFabricator(Generic[S]):
  """
  The Steel Fabricator class handles the configuration and instantiation
  of structural steel objects. The class adopts the Static Factory Pattern
  providing a single convenient API to generate Steel for Life 'Blue Book'
  sections.
  """

  @classmethod
  def _load_section_data_for(
    cls, category: SectionCategory
  ) -> dict[SectionDesignation, SectionProperties]:
    """
    Returns the properties and dimensions for all sections in a given category,
    as defined in the Steel for Life 'Blue Book'.

    Args:
      category: The selected 'Blue Book' steel section category.

    Returns:
      The full collection of steel sections in the category, as a dictionary.

    Raises:
      SectionCategoryNotFound: If the specified category is unsupported.
      FileNotFoundError: If the requested Blue Book JSON data file is missing.
    """

    dir_path = pathlib.Path(__file__).parent / ".d/bluebook/properties"

    categories = {
      SectionCategory.UB: dir_path / "ub.json",
      SectionCategory.UC: dir_path / "uc.json",
      SectionCategory.PFC: dir_path / "pfc.json",
      SectionCategory.UBP: dir_path / "ubp.json",
      SectionCategory.EQUAL_L: dir_path / "equal-l.json",
      SectionCategory.UNEQUAL_L: dir_path / "unequal-l.json",
      SectionCategory.COLD_FORMED_CHS: dir_path / "cf-chs.json",
      SectionCategory.COLD_FORMED_RHS: dir_path / "cf-rhs.json",
      SectionCategory.COLD_FORMED_SHS: dir_path / "cf-shs.json",
      SectionCategory.HOT_FORMED_CHS: dir_path / "hf-chs.json",
      SectionCategory.HOT_FORMED_RHS: dir_path / "hf-rhs.json",
      SectionCategory.HOT_FORMED_SHS: dir_path / "hf-shs.json",
      SectionCategory.HOT_FORMED_EHS: dir_path / "hf-ehs.json",
      SectionCategory.T_SPLIT_FROM_UB: dir_path / "t-split-from-ub.json",
      SectionCategory.T_SPLIT_FROM_UC: dir_path / "t-split-from-uc.json",
    }

    if category not in categories:
      raise SteelSectionCategoryNotFound(f"{category.name}.")

    file = categories[category]

    if not file.exists():
      raise FileNotFoundError(f"Section Category: {category}.")

    with open(file, "r", encoding="utf-8") as sections:
      return json.load(sections)

  # @classmethod
  # def _inject_carbon_data(cls, definitions: dict[SectionDesignation, SectionProperties]) -> dict[SectionDesignation, SectionProperties]:
  #   """
  #   For each structural section listed in the section definitions,
  #   proceed to compute the mass of carbon per unit length and then
  #   update the section definition with this new property.

  #   :param SectionDefinitions definitions: A dictionary structure containing the
  #   full collection of steel section data for a given Blue Book category.
  #   :return: The original SectionDefinitions object modified 'inplace' to augment
  #   the dictionary structure with 'Carbon Per Metre (CO2/m)' properties.
  #   """

  #   for section_properties in definitions.values():
  #       carbon_per_metre = (
  #           section_properties["Mass Per Metre (kg/m)"] *
  #           MILD_STEEL.carbon_per_kg
  #       )
  #       section_properties["Carbon Per Metre (CO2/m)"] = carbon_per_metre

  #   return definitions

  @classmethod
  def _get_sections_and_constructor_for(
    cls, category: SectionCategory
  ) -> Tuple[S, dict[SectionDesignation, SectionProperties]]:
    """
    :param SectionCategory category: Selected 'Blue Book' steel section category.
    :return: A tuple containing the constructor and steel section collection.
    :raises SectionCategoryNotFound: If the specified category is not supported.
    """

    constructors: dict[SectionCategory, S] = {
      SectionCategory.UB: UniversalBeam,
      SectionCategory.UC: UniversalColumn,
      SectionCategory.UBP: UniversalBearingPile,
      SectionCategory.HOT_FORMED_RHS: HotFormedRectangularHollowSection,
      SectionCategory.HOT_FORMED_SHS: HotFormedSquareHollowSection,
      SectionCategory.HOT_FORMED_CHS: HotFormedCircularHollowSection,
      SectionCategory.HOT_FORMED_EHS: HotFormedEllipticalHollowSection,
      SectionCategory.COLD_FORMED_RHS: ColdFormedRectangularHollowSection,
      SectionCategory.COLD_FORMED_SHS: ColdFormedSquareHollowSection,
      SectionCategory.COLD_FORMED_CHS: ColdFormedCircularHollowSection,
    }

    if category not in constructors:
      raise SteelSectionCategoryNotFound(f"{category}.")

    ctor = constructors[category]
    sections = cls._load_section_data_for(category)
    # mutate(sections, [cls._inject_carbon_data])

    return ctor, sections

  @classmethod
  def make_section(
    cls,
    category: SectionCategory,
    designation: SectionDesignation,
    length: Metre = Metre(1.0),
  ) -> S:
    """
    Instantiate a specific steel section from a given category. For the full
    list of available steel section designations, the user is advised to
    consult the Steel for Life 'Blue Book' website: https://www.steelforlifebluebook.co.uk.

    Args:
      category: Selected 'Blue Book' steel section category.
      designation: Unique identifier for the steel section.
      length: The desired steel section length (defaults to 1.0m).

    Returns:
      Single steel section of given category with the specified designation.

    Raises:
      SectionDesignationNotFound: If unsupported designation is provided.
    """

    (ctor, sections) = cls._get_sections_and_constructor_for(category)

    if designation not in sections:
      raise SteelSectionDesignationNotFound(f"{designation}.")

    return ctor(designation, sections[designation], length)

  @classmethod
  def make_all_sections(
    cls, category: SectionCategory, length: Metre = Metre(1.0)
  ) -> SteelSections[S]:
    """
    Instantiates the full collection of steel sections for a given category.
    For the full list of available steel section categories, the user is
    advised to consult the Steel for Life 'Blue Book' website: https://www.steelforlifebluebook.co.uk.

    Args:
      category: Selected 'Blue Book' steel section category.
      length: The desired length for all steel sections.

    Returns:
      A list of steel section objects.
    """

    (ctor, sections) = cls._get_sections_and_constructor_for(category)
    return SteelSections([ctor(d, sections[d], length) for d in sections.keys()])
