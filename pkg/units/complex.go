package units

import (
	"github.com/calcpadstudio/gazelle/pkg/geometry"
	"golang.org/x/exp/constraints"
)

type Volume[L Length[T], T constraints.Float] struct {
	Value L
}

type SurfaceArea[L Length[T], T constraints.Float] struct {
	Value L
}

func (s SurfaceArea[L, T]) PerMetre(length geometry.Length[L, T]) L {
	return L{Value: s.Value / length.Value}
}

func NewVolume[L Length[N], N constraints.Float](value N) Volume[L, N] {
	l := L{Value: value}
	return Volume[L, N]{Value: l}
}
