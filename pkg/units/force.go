package units

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

// The metric unit of force.
type Newton[T constraints.Float] struct {
	Value T
}

// The metric unit of force.
type Kilonewton[T constraints.Float] struct {
	Value T
}

// A union type that represents the
// combined set of units of force.
type Force[T constraints.Float] interface {
	Newton[T] | Kilonewton[T]
}

// Convert metric Newtons to Kilonewtons.
func (N Newton[T]) ToKilonewton() Kilonewton[T] {
	return Kilonewton[T]{Value: N.Value / 1000.0}
}

// Convert metric Kilonewtons to Newtons.
func (kN Kilonewton[T]) ToNewton() Newton[T] {
	return Newton[T]{Value: kN.Value * 1000.0}
}

func (N Newton[T]) String() string {
	return fmt.Sprintf("%f Newton(s)", N.Value)
}

func (kN Kilonewton[T]) String() string {
	return fmt.Sprintf("%f Kilonewton(s)", kN.Value)
}
