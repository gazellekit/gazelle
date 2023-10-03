package units

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

// The metric unit of mass.
type Gram[T constraints.Float] struct {
	Value T
}

// The metric unit of mass.
type Kilogram[T constraints.Float] struct {
	Value T
}

// The metric unit of mass.
type Tonne[T constraints.Float] struct {
	Value T
}

// A union type that represents the
// combined set of units of mass.
type Mass[T constraints.Float] interface {
	Gram[T] | Kilogram[T] | Tonne[T]
}

// Convert metric Grams to Kilograms.
func (g Gram[T]) ToKilogram() Kilogram[T] {
	return Kilogram[T]{Value: g.Value / 1000.0}
}

// Convert metric Kilograms to Grams.
func (kg Kilogram[T]) ToGram() Gram[T] {
	return Gram[T]{Value: kg.Value * 1000.0}
}

// Convert metric Grams to Tonnes.
func (g Gram[T]) ToTonne() Tonne[T] {
	return Tonne[T]{Value: g.Value / 1_000_000.0}
}

// Convert metric Kilograms to Tonnes.
func (kg Kilogram[T]) ToTonne() Tonne[T] {
	return Tonne[T]{Value: kg.Value / 1000.0}
}

// Convert metric Tonnes to Grams.
func (t Tonne[T]) ToGram() Gram[T] {
	return Gram[T]{Value: t.Value * 1_000_000.0}
}

// Convert metric Tonnes to Kilograms.
func (t Tonne[T]) ToKilogram() Kilogram[T] {
	return Kilogram[T]{Value: t.Value * 1000.0}
}

func (g Gram[T]) String() string {
	return fmt.Sprintf("%f Gram(s)", g.Value)
}

func (kg Kilogram[T]) String() string {
	return fmt.Sprintf("%f Kilogram(s)", kg.Value)
}

func (t Tonne[T]) String() string {
	return fmt.Sprintf("%f Tonne(s)", t.Value)
}
