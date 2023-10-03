package units

import (
	"fmt"
)

type Gram float64
type Kilogram float64
type Tonne float64

type Mass interface {
	Gram | Kilogram | Tonne
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
