package units

import (
	"fmt"
)

type Newton float64
type Kilonewton float64

type Force interface {
	Newton | Kilonewton
}

func (N Newton) ToKilonewton() Kilonewton {
	return Kilonewton(N / 1000.0)
}

func (N Newton) String() string {
	return fmt.Sprintf("%f Newton(s)", N)
}

func (kN Kilonewton) ToNewton() Newton {
	return Newton(kN * 1000.0)
}

func (kN Kilonewton) String() string {
	return fmt.Sprintf("%f Kilonewton(s)", kN)
}
