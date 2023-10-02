package units

import (
	"golang.org/x/exp/constraints"
)

type Metre[T constraints.Float] struct {
	Value T
}

type Millimetre[T constraints.Float] struct {
	Value T
}

type Length[T constraints.Float] interface {
	Metre[T] | Millimetre[T]
}

func (m Metre[T]) ToMillimetre() Millimetre[T] {
	return Millimetre[T]{Value: m.Value * 1000.0}
}

func (mm Millimetre[T]) ToMetre() Metre[T] {
	return Metre[T]{Value: mm.Value / 1000.0}
}
