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


from typing import Callable, TypeVar


T = TypeVar("T")

def mutate(data: T, transforms: list[Callable[[T], T]]) -> T:
  """
    Apply list of inplace transformations to object.

    Args:
      data: The original object to be transformed.
      transforms: The transformation functions to apply to the original object.

    Returns:
      The original object modified 'inplace' by the list of transformations.

  """

  for transform in transforms:
      data = transform(data)

  return data
