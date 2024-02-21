# Gazelle: a fast, cross-platform engine for structural analysis & design.
# Copyright (C) 2024 James S. Bayley
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


"""
The Steel for Life 'Blue Book' is the standard tome used by Structural Engineers 
in the UK to design and specify structural steel sections. The book contains
a plethora of design data that is fundamental to steel design in accordance with 
Eurocode 3 (EC3).

This module provides a convenient API interface to interact with, and transform, 
the data captured within the Blue Book. Data has been sourced from the official
website: https://www.steelforlifebluebook.co.uk.
"""

import json
import pathlib
from enum import Enum
from typing import Generic, Tuple

from gazelle.steel.errors import (
  SteelSectionCategoryNotFound,
  SteelSectionDesignationNotFound
)
from gazelle.steel.sections.abc import (
  SectionDesignation,
  SectionProperties
)
from gazelle.steel.sections.collections import (
  S,
  SteelSections
)
from gazelle.steel.sections.hollow import (
  ColdFormedCircularHollowSection,
  ColdFormedRectangularHollowSection,
  ColdFormedSquareHollowSection,
  HotFormedCircularHollowSection,
  HotFormedEllipticalHollowSection,
  HotFormedRectangularHollowSection,
  HotFormedSquareHollowSection
)

from gazelle.steel.sections.universal import (
  UniversalBeam,
  UniversalColumn,
  UniversalBearingPile
)
from gazelle.units import (
  Metre
)


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


class SteelFabricator(Generic[S]):
  """
  The Steel Fabricator class handles the configuration and instantiation
  of structural steel objects. The class adopts the Static Factory Pattern
  providing a single convenient API to generate Steel for Life 'Blue Book'
  sections.
  """

  @classmethod
  def _load_section_data_for(cls, category: SectionCategory) -> dict[SectionDesignation, SectionProperties]:
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

    dir_path = pathlib.Path(__file__).parent.parent / ".d/bluebook/properties"

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
  def _get_sections_and_constructor_for(cls, category: SectionCategory) -> Tuple[S, dict[SectionDesignation, SectionProperties]]:
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
          SectionCategory.COLD_FORMED_CHS: ColdFormedCircularHollowSection
      }

      if category not in constructors:
          raise SteelSectionCategoryNotFound(f"{category}.")

      ctor = constructors[category]
      sections = cls._load_section_data_for(category)
      # mutate(sections, [cls._inject_carbon_data])

      return ctor, sections


  @classmethod
  def make_section(cls, category: SectionCategory, designation: SectionDesignation, length: Metre = Metre(1.0)) -> S:
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
  def make_all_sections(cls, category: SectionCategory, length: Metre = Metre(1.0)) -> SteelSections[S]:
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
