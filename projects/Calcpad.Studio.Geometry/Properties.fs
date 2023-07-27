// Robust, Transparent Structural Design.
// Copyright (C) 2023  James S. Bayley
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published
// by the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.


namespace Calcpad.Studio.Geometry

/// <summary>
/// Orthogonal geometric axis.
/// </summary>
type Axis =
    | X
    | Y

/// <summary>
/// Orthogonal axis about which rotation occurs.
/// </summary>
type RotationalAxis =
    | XX
    | YY

/// <summary>
/// Length dimension annotated with unit-of-measure.
/// </summary>
type Length<[<Measure>] 'TUnit> = Length of float<'TUnit>

/// <summary>
/// Width dimension annotated with unit-of-measure.
/// </summary>
type Width<[<Measure>] 'TUnit> = Width of float<'TUnit>

/// <summary>
/// Depth dimension annotated with unit-of-measure.
/// </summary>
type Depth<[<Measure>] 'TUnit> = Depth of float<'TUnit>

/// <summary>
/// Diameter dimension annotated with unit-of-measure.
/// </summary>
type Diameter<[<Measure>] 'TUnit> = Diameter of float<'TUnit>

/// <summary>
/// Perimeter dimension annotated with unit-of-measure.
/// </summary>
type Perimeter<[<Measure>] 'TUnit> = Perimeter of float<'TUnit>

/// <summary>
/// Area dimension annotated with unit-of-measure.
/// Union type represents possible area semantics.
/// </summary>
type Area<[<Measure>] 'TUnit> =
    | CrossSectionalArea of float<'TUnit^2>
    | SurfaceArea of float<'TUnit^2>

/// <summary>
/// Volume dimension annotated with unit-of-measure.
/// </summary>
type Volume<[<Measure>] 'TUnit> = Volume of float<'TUnit^3>

/// <summary>
/// Second moment of area dimension annotated with unit-of-measure.
/// </summary>
type SecondMomentOfArea<[<Measure>] 'TUnit> = SecondMomentOfArea of float<'TUnit^4>
