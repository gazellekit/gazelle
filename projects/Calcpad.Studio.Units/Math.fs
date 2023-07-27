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
/// Collection of mathematical modules that operate on
/// values with unit-of-measure type annotations.
/// </summary>
[<RequireQualifiedAccess>]
module Math =

    /// <summary>
    /// Unit safe exponentiation function raised to the power of 2.
    /// </summary>
    /// <param name="n">Original value.</param>
    /// <returns>Value raised to the power of 2.</returns>
    let pow2 (n: float<'T>) : float<'T^2> = n * n

    /// <summary>
    /// Unit safe exponentiation function raised to the power of 3.
    /// </summary>
    /// <param name="n">Original value.</param>
    /// <returns>Value raised to the power of 3.</returns>
    let pow3 (n: float<'T>) : float<'T^3> = n * n * n

    /// <summary>
    /// Unit safe exponentiation function raised to the power of 4.
    /// </summary>
    /// <param name="n">Original value.</param>
    /// <returns>Value raised to the power of 4.</returns>
    let pow4 (n: float<'T>) : float<'T^4> = n * n * n * n
