package units

import (
	"golang.org/x/exp/constraints"
)

type Newton[T constraints.Float] struct {
	Value T
}

type Kilonewton[T constraints.Float] struct {
	Value T
}

type Force[T constraints.Float] interface {
	Newton[T] | Kilonewton[T]
}

func (N Newton[T]) ToKilonewton() Kilonewton[T] {
	return Kilonewton[T]{Value: N.Value / 1000.0}
}

func (kN Kilonewton[T]) ToNewton() Newton[T] {
	return Newton[T]{Value: kN.Value * 1000.0}
}
