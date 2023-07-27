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
/// Time in days.
/// </summary>
[<Measure>]
type days

/// <summary>
/// Length in millimetres.
/// </summary>
[<Measure>]
type mm

/// <summary>
/// Force in Kilonewtons.
/// </summary>
[<Measure>]
type kN

/// <summary>
/// Moment or Torque in Kilonewton-Metres.
/// </summary>
[<Measure>]
type kNm = kN * m

/// <summary>
/// Number of layers.
/// </summary>
[<Measure>]
type layers

/// <summary>
/// Number of bars.
/// </summary>
[<Measure>]
type bars

/// <summary>
/// Unit of density.
/// </summary>
type Density<[<Measure>] 'TMass, [<Measure>] 'TLength> = Density of float<'TMass / 'TLength^3>

/// <summary>
/// Unit of mechanical stress.
/// </summary>
type Stress<[<Measure>] 'TForce, [<Measure>] 'TLength> = Stress of float<'TForce / 'TLength^2>

/// <summary>
/// Unit of mechanical pressure.
/// </summary>
type Pressure<[<Measure>] 'TForce, [<Measure>] 'TLength> = Stress<'TForce, 'TLength>
