"""
The collection of steel section types, as
defined in the Steel for Life 'Blue Book'.
"""

from abc import abstractmethod, ABC

from gazelle.units import (
    Centimetre,
    Millimetre
)
from gazelle.steel.sections.abc import (
    SteelSection
)


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


class UniversalBeam(UniversalSection):
    def __str__(self):
        return f"Universal Beam (UB) Section: {self.designation}"


class UniversalColumn(UniversalSection):
    def __str__(self):
        return f"Universal Column (UC) Section: {self.designation}"


class UniversalBearingPile(UniversalSection):
    def __str__(self):
        return f"Universal Bearing Pile (UBP) Section: {self.designation}"
