from abc import abstractmethod, ABC

from gazelle.steel.sections.abc import SteelSection
from gazelle.units import Millimetre


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

            }
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
            }
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
            }
        }

    @abstractmethod
    def __str__(self):
        pass


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
