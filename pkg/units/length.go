package units

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

// The metric unit of length.
type Metre[T constraints.Float] struct {
	Value T
}

// The metric unit of length.
type Millimetre[T constraints.Float] struct {
	Value T
}

// A union type that represents the
// combined set of units of length.
type Length[T constraints.Float] interface {
	Metre[T] | Millimetre[T]
}

// Convert metric Metres to Millimetres.
func (m Metre[T]) ToMillimetre() Millimetre[T] {
	return Millimetre[T]{Value: m.Value * 1000.0}
}

// Convert metric Millimetres to Metres.
func (mm Millimetre[T]) ToMetre() Metre[T] {
	return Metre[T]{Value: mm.Value / 1000.0}
}

func (m Metre[T]) String() string {
	return fmt.Sprintf("%f Metre(s)", m.Value)
}

func (m Millimetre[T]) String() string {
	return fmt.Sprintf("%f Millimetre(s)", m.Value)
}
