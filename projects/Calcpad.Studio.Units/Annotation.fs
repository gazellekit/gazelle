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


namespace Calcpad.Studio.Units

/// <summary>
/// Remove unit-of-measure type annotations from various types.
/// </summary>
[<RequireQualifiedAccess>]
module RemoveUnits =

    /// <summary>
    /// Remove unit-of-measure type annotation from 32-bit integer.
    /// </summary>
    /// <param name="value">Annotated 32-bit integer.</param>
    /// <returns>Value without unit-of-measure.</returns>
    let fromInt32 (value: int<'T>) : int = int value

    /// <summary>
    /// Remove unit-of-measure type annotation from float.
    /// </summary>
    /// <param name="value">Annotated float.</param>
    /// <returns>Value without unit-of-measure.</returns>
    let fromFloat (value: float<'T>) : float = float value

/// <summary>
/// Add unit-of-measure type annotations to various types.
/// </summary>
[<RequireQualifiedAccess>]
module AddUnits =

    /// <summary>
    /// Add unit-of-measure type annotation to 32-bit integer.
    /// </summary>
    /// <param name="value">Primitive 32-bit integer.</param>
    /// <returns>Value annotated with unit-of-measure.</returns>
    let toInt32 (value: int) : int<'T> =
        LanguagePrimitives.Int32WithMeasure value

    /// <summary>
    /// Add unit-of-measure type annotation to float.
    /// </summary>
    /// <param name="value">Primitive float.</param>
    /// <returns>Value annotated with unit-of-measure.</returns>
    let toFloat (value: float) : float<'T> =
        LanguagePrimitives.FloatWithMeasure value
