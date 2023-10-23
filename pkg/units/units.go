package units

import (
	"fmt"
)

type Gram float64
type Kilogram float64
type Tonne float64
type Metre float64
type Millimetre float64
type Newton float64
type Kilonewton float64
type Area float64
type Perimeter float64
type SurfaceArea float64
type Volume float64

type SecondMomentOfArea struct {
	XX, YY float64
}

type RadiusOfGyration struct {
	XX, YY float64
}

func (g Gram) ToKilogram() Kilogram {
	return Kilogram(g / 1000.0)
}

func (g Gram) ToTonne() Tonne {
	return Tonne(g / 1_000_000.0)
}

func (g Gram) String() string {
	return fmt.Sprintf("%f Gram(s)", g)
}

func (kg Kilogram) ToGram() Gram {
	return Gram(kg * 1000.0)
}

func (kg Kilogram) ToTonne() Tonne {
	return Tonne(kg / 1000.0)
}

func (kg Kilogram) String() string {
	return fmt.Sprintf("%f Kilogram(s)", kg)
}

func (t Tonne) ToGram() Gram {
	return Gram(t * 1_000_000.0)
}

func (t Tonne) ToKilogram() Kilogram {
	return Kilogram(t * 1000.0)
}

func (t Tonne) String() string {
	return fmt.Sprintf("%f Tonne(s)", t)
}

func (m Metre) ToMillimetre() Millimetre {
	return Millimetre(m * 1000.0)
}

func (m Metre) String() string {
	return fmt.Sprintf("%f Metre(s)", m)
}

func (mm Millimetre) ToMetre() Metre {
	return Metre(mm / 1000.0)
}

func (m Millimetre) String() string {
	return fmt.Sprintf("%f Millimetre(s)", m)
}

func (N Newton) ToKilonewton() Kilonewton {
	return Kilonewton(N / 1000.0)
}

func (N Newton) String() string {
	return fmt.Sprintf("%f Newton(s)", N)
}

func (kN Kilonewton) ToNewton() Newton {
	return Newton(kN * 1000.0)
}

func (kN Kilonewton) String() string {
	return fmt.Sprintf("%f Kilonewton(s)", kN)
}
