package units

import (
	"golang.org/x/exp/constraints"
)

type Gram[T constraints.Float] struct {
	Value T
}

type Kilogram[T constraints.Float] struct {
	Value T
}

type Tonne[T constraints.Float] struct {
	Value T
}

type Mass[T constraints.Float] interface {
	Gram[T] | Kilogram[T] | Tonne[T]
}

func (g Gram[T]) ToKilogram() Kilogram[T] {
	return Kilogram[T]{Value: g.Value / 1000.0}
}

func (kg Kilogram[T]) ToGram() Gram[T] {
	return Gram[T]{Value: kg.Value * 1000.0}
}

func (g Gram[T]) ToTonne() Tonne[T] {
	return Tonne[T]{Value: g.Value / 1_000_000.0}
}

func (kg Kilogram[T]) ToTonne() Tonne[T] {
	return Tonne[T]{Value: kg.Value / 1000.0}
}

func (t Tonne[T]) ToGram() Gram[T] {
	return Gram[T]{Value: t.Value * 1_000_000.0}
}

func (t Tonne[T]) ToKilogram() Kilogram[T] {
	return Kilogram[T]{Value: t.Value * 1000.0}
}
