package steel

import (
	bluebook "github.com/calcpadstudio/gazelle/pkg/bluebook"
)

type UniversalBeam struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties bluebook.DimensionsAndProperties
}

type UniversalColumn struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties bluebook.DimensionsAndProperties
}

type UniversalBearingPile struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties bluebook.DimensionsAndProperties
}

func (UniversalBeam) String() string {
	return "Universal Beam"
}

func (UniversalColumn) String() string {
	return "Universal Column"
}

func (UniversalBearingPile) String() string {
	return "Universal Bearing Pile"
}
