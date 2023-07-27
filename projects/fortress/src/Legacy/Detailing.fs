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


namespace Calcpad.Studio.Fortress

//open System

///// Centre-to-centre spacing between adjacent bars/links.
//type BarSpacing = BarSpacing of float<mm>

///// Space between bars, measured between the outermost bar dimensions.
//type ClearSpace = ClearSpace of float<mm>

///// Total number of reinforcing bars.
//type NumberOfBars = NumberOfBars of int<bars>

//// Lightweight records specifying rebar configuration.
//type NumberOfBarsAndBarSize = { NumberOfBars: NumberOfBars; BarSize: BarSize }
//type LinkSpacingAndLinkSize = { LinkSpacing: BarSpacing; LinkSize: BarSize }

//module Detailing =

//    /// Returns no. of intermediate bars along a given length at the prescribed spacing.
//    /// This does NOT consider bars at the start or end (i.e. at x = 0 and x = L).
//    /// For a 1000mm length at 250mm spacing, the equations returns 3 intermediate bars.
//    let getNumberOfIntermediateBars (BarSpacing sp) (Length l) =
//        int (Math.Ceiling (l / sp)) - 1
//        |> AddUnitsToInteger32
//        |> NumberOfBars

//    /// Calculates bar spacing for intermediate bars along a given length.
//    /// This does NOT consider bars at the start or end (i.e. at x = 0 and x = L).
//    /// For a 1000mm length with 3 inner bars and 2 end bars (5 bars in total),
//    /// the equation ignores the end bars and returns a spacing of 250mm.
//    let getIntermediateBarSpacing (NumberOfBars n) (Length l) = BarSpacing (l / (float n + 1.0))

//    /// Returns the minimum permissible clear spacing between adjacent bars.
//    let getMinimumClearBarSpacing (barSize: BarSize) = ClearSpace barSize.diameter

//    /// Calculates clear spacing between two straight bars by comparing the pythagorean
//    /// distance between their respective cross-section centroids in 3D space.
//    let clearSpaceBetweenBars (bar1: StraightBar) (bar2: StraightBar) =
//        let p1 = bar1.Geometry.StartPoint
//        let p2 = bar2.Geometry.StartPoint
//        let halfΦ1 = (bar1.BarSize.diameter / 2.0) |> UnitAnnotation.stripUnitsFromFloat
//        let halfΦ2 = (bar2.BarSize.diameter / 2.0) |> UnitAnnotation.stripUnitsFromFloat
//        (distanceBetweenPoints p1 p2) - (halfΦ1 + halfΦ2)
//        |> AddUnitsToFloat

//    // Union type helper methods.
//    let internal unwrapBarSpacing (BarSpacing sp) = sp
//    let internal unwrapClearSpace (ClearSpace sp) = sp
