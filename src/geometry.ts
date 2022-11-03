// Structures.js - For Structural Engineers, Everywhere.
// Copyright (C) 2022  James S. Bayley
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

/** The orthogonal axes about which flexure (i.e. bending) occurs. */
export type FlexuralAxis = "X-X" | "Y-Y";

/** Represents a generic 2D geometry. */
export interface I2Dimensional {
  /** The geometric area. */
  area: () => number;

  /** The geometric perimeter. */
  perimeter: () => number;

  /**
   * The geometric second moment of area about a given axis.
   * @param rotationAbout the axis about which the section bends.
   */
  secondMomentOfArea: (rotationAbout: FlexuralAxis) => number;
}

/** Represents a generic 3D geometry. */
export interface I3Dimensional {
  /** The geometric volume. */
  volume: () => number;
}

/** A basic 2D rectangular geometry. */
export class Rectangle implements I2Dimensional {
  /** The geometric width (parallel to local x-axis). */
  public readonly width: number;

  /** The geometric depth (parallel to local y-axis). */
  public readonly depth: number;

  /**
   * Initialise instance of a Rectangle.
   * @param width the geometric width (parallel to local x-axis).
   * @param depth the geometric depth (parallel to local y-axis).
   */
  public constructor(width: number, depth: number) {
    if (width <= 0.0) {
      throw new Error("Width must be greater than 0.");
    }

    if (depth <= 0.0) {
      throw new Error("Depth must be greater than 0.");
    }

    this.width = width;
    this.depth = depth;
  }

  public area(): number {
    return this.width * this.depth;
  }

  public perimeter(): number {
    return 2 * this.width + 2 * this.depth;
  }

  public secondMomentOfArea(rotationAbout: FlexuralAxis): number {
    switch (rotationAbout) {
      case "X-X": {
        return (this.width * Math.pow(this.depth, 3)) / 12.0;
      }
      case "Y-Y": {
        return (this.depth * Math.pow(this.width, 3)) / 12.0;
      }
    }
  }
}

/** A basic 2D circular geometry. */
export class Circle implements I2Dimensional {
  /** The geometric diameter. */
  public readonly diameter: number;

  /** The geometric radius. */
  public readonly radius: number;

  /**
   * Initialise instance of a Circle.
   * @param diameter the geometric diameter.
   */
  public constructor(diameter: number) {
    if (diameter <= 0.0) {
      throw new Error("Diameter must be greater than 0.");
    }

    this.diameter = diameter;
    this.radius = this.diameter / 2.0;
  }

  public area(): number {
    return (Math.PI * Math.pow(this.diameter, 2)) / 4.0;
  }

  public perimeter(): number {
    return Math.PI * this.diameter;
  }

  public secondMomentOfArea(_: FlexuralAxis): number {
    return (Math.PI * Math.pow(this.diameter, 4)) / 64;
  }
}
