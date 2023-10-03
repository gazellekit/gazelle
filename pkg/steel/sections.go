package steel

import (
	bluebook "github.com/calcpadstudio/gazelle/pkg/bluebook"
	units "github.com/calcpadstudio/gazelle/pkg/units"
	"golang.org/x/exp/constraints"
)

type UniversalBeam[L units.Length[T], M units.Mass[T], T constraints.Float] struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties bluebook.DimensionsAndProperties[L, M, T]
}

type UniversalColumn[L units.Length[T], M units.Mass[T], T constraints.Float] struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties bluebook.DimensionsAndProperties[L, M, T]
}

type UniversalBearingPile[L units.Length[T], M units.Mass[T], T constraints.Float] struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties bluebook.DimensionsAndProperties[L, M, T]
}

func (UniversalBeam[L, M, T]) String() string {
	return "Universal Beam"
}

func (UniversalColumn[L, M, T]) String() string {
	return "Universal Column"
}

func (UniversalBearingPile[L, M, T]) String() string {
	return "Universal Bearing Pile"
}
