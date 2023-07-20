type FlexuralAxis = 'X-X' | 'Y-Y';

export class Rectangle {
  public constructor(public width: number, public height: number) {
    if (width < 0) {
      throw new Error(`Width must be greater than zero.`);
    }

    if (height < 0) {
      throw new Error(`Height must be greater than zero.`);
    }

    this.width = width;
    this.height = height;
  }

  public area(): number {
    return this.width * this.height;
  }

  public perimeter(): number {
    return 2 * (this.width + this.height);
  }

  public secondMomentOfArea(axis: FlexuralAxis): number {
    switch (axis) {
      case 'X-X':
        return this.width * (this.height ** 3) / 12;
      case 'Y-Y':
        return this.height * (this.width ** 3) / 12;
    }
  }
}

export class Circle {
  public constructor(public diameter: number) {
    if (diameter < 0) {
      throw new Error(`Width must be greater than zero.`);
    }

    this.diameter = diameter;
  }

  public area(): number {
    return Math.PI * (this.diameter ** 2) / 4;
  }

  public perimeter(): number {
    return Math.PI * this.diameter;
  }

  public secondMomentOfArea(axis: FlexuralAxis): number {
    switch (axis) {
      case 'X-X':
      case 'Y-Y':
        return Math.PI * (this.diameter ** 4) / 64;
    }
  }
}