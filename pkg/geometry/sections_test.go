package geometry

import (
	"fmt"
	"testing"
)

func TestUniversalBeam(t *testing.T) {
	ub := UniversalBeam{}
	fmt.Println(ub)
	fmt.Println(ub.DimensionsAndProperties.Depth)
	fmt.Println(ub.DimensionsAndProperties.RadiusOfGyration.XX)
}
