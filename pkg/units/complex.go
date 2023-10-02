package units

import (
	"golang.org/x/exp/constraints"
)

// A complex type that represents a volumetric
// quantity. It is bound to a specific length
// derivation (e.g., Metre, Millimetre etc.)
// to avoid incompatible unit combinations.
type Volume[L Length[T], T constraints.Float] struct {
	value L
}

// Retrieves the underlying value encapsulated
// by the complex Volume type. The returned
// value represents the specific numeric
// type bound by the Generic at runtime. In
// the case that an unsupported unit derivation
// is bound to the Generic parameter, an error
// is returned.
func (v Volume[L, T]) GetValue() T {
	switch x := any(v.value).(type) {
	case Metre[T]:
		return x.Value
	case Millimetre[T]:
		return x.Value
	default:
		panic("Error!")
		// return error('')
	}
}

// A complex type that represents a Surface
// Area. It is bound to a specific length
// derivation (e.g., Metre, Millimetre etc.)
// to avoid incompatible unit combinations.
type SurfaceArea[L Length[T], T constraints.Float] struct {
	value L
}

// Retrieves the underlying value encapsulated
// by the complex Surface Area type. The returned
// value represents the specific numeric type
// bound by the Generic at runtime. In the case
// that an unsupported unit derivation is bound
// to the Generic parameter, an error is returned.
func (v SurfaceArea[L, T]) GetValue() T {
	switch x := any(v.value).(type) {
	case Metre[T]:
		return x.Value
	case Millimetre[T]:
		return x.Value
	default:
		panic("Error!")
	}
}

// func NewVolume[L Length[N], N constraints.Float](value N) Volume[L, N] {
// 	l := L{Value: value}
// 	return Volume[L, N]{Value: l}
// }
