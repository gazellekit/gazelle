"""
Abstract base class representations common to all steel sections. 

Typically, users will not use this module directly. All 'concrete' 
steel sections implemented elsewhere within the package inherit 
from classes within this module. Users can reliably depend on the 
attributes and methods defined herein as the public interface 
for all steel sections and collections of steel sections.

Nevertheless, specific steel section types do provide more 
specialised, refined implementations and additional attributes.
Therefore, if a particular attribute has not been defined 
within the abstract base classes, it is worth checking the
specific section implementations.

The real advantage of this module is that it provides generic
behaviours that are common to all steel sections, regardless
of their specific geometries. For example, all steel sections 
have a 'mass per metre length', hence it is sensible to capture 
this behaviour at the top of the class hierarchy.
"""

from abc import ABC, abstractmethod
from typing import NewType, Union

from gazelle.units import (
    Area,
    Carbon,
    Centimetre,
    Kilogram,
    Mass,
    Metre,
    SurfaceArea,
    Tonne
)


SectionDesignation = NewType("SectionDesignation", str)
SectionProperties = NewType("SectionProperties", dict[str, Union[bool, float]])


class SteelSection(ABC):
    """An abstract class for a steel section."""

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
        return SurfaceArea(self._properties["Surface Area Per Metre (m2)"], Metre) \
            .per_unit_length(Metre)

    @property
    def surface_area_per_tonne(self) -> SurfaceArea.PerUnitMass[Metre, Tonne]:
        """The surface area per tonne of the section."""
        return SurfaceArea(self._properties["Surface Area Per Tonne (m2)"], Metre) \
            .per_unit_mass(Tonne)

    @property
    def carbon_per_metre(self) -> Carbon.PerUnitLength[Metre]:
        """The carbon per metre length of the section."""
        return Carbon(self._properties["Carbon Per Metre (CO2/m)"]) \
            .per_unit_length(Metre)

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
            }
        }

    @abstractmethod
    def __str__(self) -> str:
        pass
