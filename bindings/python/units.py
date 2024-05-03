# SPDX-License-Identifier: AGPL-3.0-or-later
# Gazelle: A fast engine for civil engineering design.
# Copyright (C) 2024 James S. Bayley


from abc import ABC
from math import pi
from typing import Generic, Type, TypeVar, Union

M = TypeVar("M", bound="Mass")
L = TypeVar("L", bound="Length")
L2 = TypeVar("L2", bound="Length")
T = TypeVar("T", bound="Dimension")
U = TypeVar("U", bound="Dimension")
W = TypeVar("W", bound="Dimension")


class Ratio:
  def __init__(self, value: float):
    if value >= 0.0:
      self._dtype = type(self)
      self.value = value
      self.units = None
    else:
      raise ValueError(f"{self.__class__.__name__} < 0.")

  def to_json(self):
    return {"value": f"{self.value:.2f}", "units": self.units}


class Dimension(Ratio, ABC):
  def __init__(self, value: float):
    super().__init__(value)

  def __repr__(self) -> str:
    return f"{self.value:.2f} {self.units}"


class Length(Dimension, ABC):
  def __init__(self, value: float):
    super().__init__(value)

  def __mul__(self: L, other: L) -> "Area[L]":
    if type(self) is type(other):
      return Area(self.value * other.value, type(self))
    raise TypeError(f"Incompatible: {type(self)} and {type(other)}.")


class Mass(Dimension, ABC):
  def __init__(self, value: float):
    super().__init__(value)

  def __truediv__(self: M, volume: "Volume[L]") -> "Density[M, L]":
    return Density(self, volume)

  def per_unit_length(self, unit_length: Type[L]) -> "Mass.PerUnitLength[L]":
    return Mass.PerUnitLength(self, unit_length)

  class PerUnitLength(Dimension, Generic[M, L]):
    def __init__(self, mass: M, unit_length: Type[L]):
      super().__init__(mass.value)
      self._dtype = (mass._dtype, unit_length(1)._dtype)
      self.units = f"{self._dtype[0](1).units}/{self._dtype[1](1).units}"

    def __mul__(self, other: L) -> M:
      if self._dtype[1] is other._dtype:
        return self._dtype[0](self.value * other.value)
      raise TypeError(f"Incompatible: {self._dtype[1]} and {other._dtype}.")


class Area(Dimension, Generic[L]):
  def __init__(self, value: float, dtype: Type[L]):
    super().__init__(value)
    self._dtype = dtype
    self.units = f"{self._dtype(1).units}^2"

  @classmethod
  def from_rectangle(cls, width: L, depth: L) -> "Area[L]":
    if type(width) is type(depth):
      return width * depth
    raise TypeError(f"Incompatible: {type(width)} and {type(depth)}.")

  @classmethod
  def from_circle(cls, diameter: L) -> "Area[L]":
    area = (pi * diameter.value**2.0) / 4.0
    return cls(area, type(diameter))

  def __mul__(self: "Area[L]", length: L) -> "Volume[L]":
    if self._dtype is type(length):
      return Volume(self.value * length.value, self._dtype)
    raise TypeError(f"Incompatible: {type(length)} and {self._dtype}.")


class SurfaceArea(Dimension, Generic[L]):
  def __init__(self, value: float, dtype: Type[L]):
    super().__init__(value)
    self._dtype = dtype
    self.units = f"{self._dtype(1).units}^2"

  def per_unit_length(
    self, unit_length: Type[L2]
  ) -> "SurfaceArea.PerUnitLength[L, L2]":
    return SurfaceArea.PerUnitLength(self, unit_length)

  def per_unit_mass(self, unit_mass: Type[M]) -> "SurfaceArea.PerUnitMass[L, M]":
    return SurfaceArea.PerUnitMass(self, unit_mass)

  @classmethod
  def from_cuboid(cls, width: L, depth: L, length: L) -> "SurfaceArea[L]":
    if type(width) is type(depth) and type(width) is type(length):
      perimeter = (2 * width.value) + (2 * depth.value)
      surface_area = perimeter * length.value
      return cls(surface_area, type(width))
    raise TypeError(f"Incompatible: {type(width)}, {type(depth)}, {type(length)}.")

  @classmethod
  def from_cylinder(cls, diameter: L, length: L) -> "SurfaceArea[L]":
    if type(diameter) is type(length):
      surface_area = pi * diameter.value * length.value
      return cls(surface_area, type(diameter))
    raise TypeError(f"Incompatible: {type(diameter)} and {type(length)}.")

  class PerUnitLength(Dimension, Generic[L, L2]):
    def __init__(self, surface_area: "SurfaceArea[L]", unit_length: Type[L2]):
      super().__init__(surface_area.value)
      self._dtype = (surface_area._dtype, unit_length(1)._dtype)
      self.units = f"{self._dtype[0](1).units}^2/{self._dtype[1](1).units}"

    def __mul__(self, length: L2) -> "SurfaceArea[L]":
      if self._dtype[1] is length._dtype:
        return SurfaceArea(self.value * length.value, self._dtype[0])
      raise TypeError(f"Incompatible: {self._dtype[1]} and {length._dtype}.")

  class PerUnitMass(Dimension, Generic[L, M]):
    def __init__(self, surface_area: "SurfaceArea[L]", unit_mass: Type[M]):
      super().__init__(surface_area.value)
      self._dtype = (surface_area._dtype, unit_mass(1)._dtype)
      self.units = f"{self._dtype[0](1).units}^2/{self._dtype[1](1).units}"

    def __mul__(self, mass: M) -> "SurfaceArea[L]":
      if self._dtype[1] is mass._dtype:
        return SurfaceArea(self.value * mass.value, self._dtype[0])
      raise TypeError(f"Incompatible: {self._dtype[1]} and {mass._dtype}.")


class Volume(Dimension, Generic[L]):
  def __init__(self, value: float, dtype: Type[L]):
    super().__init__(value)
    self._dtype = dtype
    self.units = f"{self._dtype(1).units}^3"

  @classmethod
  def from_area(cls, area: Area[L], length: L) -> "Volume[L]":
    if area._dtype is type(length):
      return area * length
    raise TypeError(f"Incompatible types: {area._dtype} and {type(length)}.")

  @classmethod
  def from_cuboid(cls, width: L, depth: L, length: L) -> "Volume[L]":
    if type(width) is type(depth) and type(width) is type(length):
      return width * depth * length
    raise TypeError(f"Incompatible: {type(width)}, {type(depth)}, {type(length)}.")

  @classmethod
  def from_cylinder(cls, diameter: L, length: L) -> "Volume[L]":
    if type(diameter) is type(length):
      return Area.from_circle(diameter) * length
    raise TypeError(f"Incompatible types: {diameter._dtype} and {length._dtype}.")

  def __truediv__(self, other: Union[Area[L], L]) -> Union[Area[L], L]:
    if self._dtype is not other._dtype:
      raise TypeError(f"Incompatible: {self._dtype} and {other._dtype}.")

    if isinstance(other, Area):
      return self._dtype(self.value / other.value)

    if isinstance(other, Length):
      return Area(self.value / other.value, self._dtype)

    raise NotImplementedError(f"Unexpected: {type(other)}.")


class Carbon(Dimension):
  def __init__(self, value):
    super().__init__(value)
    self.units = "CO2"

  def per_unit_length(self, unit_length: Type[L]) -> "Carbon.PerUnitLength[L]":
    return Carbon.PerUnitLength(self, unit_length)

  class PerUnitLength(Dimension, Generic[L]):
    def __init__(self, CO2: "Carbon", unit_length: Type[L]):
      super().__init__(CO2.value)
      self._dtype = (CO2._dtype, unit_length(1)._dtype)
      self.units = f"{self._dtype[0](1).units}/{self._dtype[1](1).units}"

    def __mul__(self, other: L) -> "Carbon":
      if self._dtype[1] is other._dtype:
        return Carbon(self.value * other.value)
      raise TypeError(f"Incompatible: {self._dtype[1]} and {other._dtype}.")


class Density(Dimension, Generic[M, L]):
  def __init__(self, mass: M, volume: Volume[L]):
    super().__init__(mass.value / volume.value)
    self._dtype = (mass._dtype, volume._dtype)
    self.units = f"{self._dtype[0](1).units}/{self._dtype[1](1).units}^3"

  def __mul__(self, other: Volume[L]) -> M:
    if self._dtype[1] is other._dtype:
      return self._dtype[0](self.value * other.value)
    raise TypeError(f"Incompatible: {self._dtype[1]} and {other._dtype}.")


class Millimetre(Length):
  def __init__(self, value):
    super().__init__(value)
    self.units = "mm"

  def to_centimetre(self) -> "Centimetre":
    return Centimetre(self.value / 10.0)

  def to_metre(self) -> "Metre":
    return Metre(self.value / 1000.0)


class Centimetre(Length):
  def __init__(self, value):
    super().__init__(value)
    self.units = "cm"

  def to_millimetre(self) -> "Metre":
    return Millimetre(self.value * 10.0)

  def to_metre(self) -> "Metre":
    return Metre(self.value / 100.0)


class Metre(Length):
  def __init__(self, value):
    super().__init__(value)
    self.units = "m"

  def to_millimetre(self) -> Millimetre:
    return Millimetre(self.value * 1000.0)

  def to_centimetre(self) -> Centimetre:
    return Centimetre(self.value * 100.0)


class Kilogram(Mass):
  def __init__(self, value):
    super().__init__(value)
    self.units = "kg"

  def to_tonne(self) -> "Tonne":
    return Tonne(self.value / 1000.0)


class Tonne(Mass):
  def __init__(self, value):
    super().__init__(value)
    self.units = "tonne"

  def to_kilogram(self) -> "Kilogram":
    return Kilogram(self.value * 1000.0)


if __name__ == "__main__":
  w = Centimetre(2.5)
  d = Centimetre(1.5)
  m = Metre(4)
  a = w * d
  kg = Kilogram(5)
  v = a * Centimetre(1)
  den = kg / v
  mpul = kg.per_unit_length(Metre)
  length = Metre(2)
  CO2 = Carbon(20)
  cpul = CO2.per_unit_length(Millimetre)
  surface_area = SurfaceArea(20.0, Millimetre)
  surface_area_per_metre = surface_area.per_unit_length(Metre)
  surface_area_per_metre.to_json()

  print(f"Width: {w}.")
  print(f"Depth: {d}.")
  print(f"Area: {a}.")
  print(f"Mass: {kg}.")
  print(f"Volume: {v}.")
  print(f"Density: {den}.")
  print(f"Density x Volume: {den * v}.")
  print(f"Length: {v / a}.")
  print(f"Vol / Width: {v / w}.")
  print(f"Kilogram Per Metre: {mpul}.")
  print(f"5kg/m x 2m: {mpul * length}")
  print(f"Carbon: {CO2}.")
  print(f"Carbon Per Metre Length: {cpul}.")
  print(f"Surface Area: {surface_area}.")
  print(f"Surface Area Per Metre Length: {surface_area_per_metre}.")
  print(f"{surface_area_per_metre.to_json()}")
  print(f"{cpul.to_json()}")
