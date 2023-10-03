package units

import (
	"fmt"
)

type Metre float64
type Millimetre float64

type Length interface {
	Metre | Millimetre
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
