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

open FSharp.Data.UnitSystems.SI.UnitSymbols

/// <summary>
/// Functions to convert unit-of-measure type annotations.
/// </summary>
[<RequireQualifiedAccess>]
module Convert =

    /// <summary>
    /// Converts millimetres to metres.
    /// </summary>
    /// <param name="n">Value in millimetres.</param>
    /// <returns>Value in metres.</returns>
    let millimetresToMetres (n: float<mm>) : float<m> = n / 1000.0<mm / m>

    /// <summary>
    /// Converts metres to millimetres.
    /// </summary>
    /// <param name="n">Value in metres.</param>
    /// <returns>Value in millimetres.</returns>
    let metresToMillimetres (n: float<m>) : float<mm> = n * 1000.0<mm / m>

    /// <summary>
    /// Converts Newtons to Kilonewtons.
    /// </summary>
    /// <param name="n">Value in Newtons.</param>
    /// <returns>Value in Kilonewtons.</returns>
    let newtonsToKilonewtons (x: float<N>) : float<kN> = x / 1000.0<N / kN>

    /// <summary>
    /// Converts Kilonewtons to Newtons.
    /// </summary>
    /// <param name="n">Value in Kilonewtons.</param>
    /// <returns>Value in Newtons.</returns>
    let kilonewtonsToNewtons (x: float<kN>) : float<N> = x * 1000.0<N / kN>
