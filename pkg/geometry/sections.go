package geometry

type DimensionsAndProperties struct {
	Depth                      float64
	Width                      float64
	Length                     float64
	TotalMass                  float64
	MassPerMetreLength         float64
	CrossSectionalArea         float64
	SurfaceAreaPerMetre        float64
	SurfaceAreaPerTonne        float64
	WebThickness               float64
	FlangeThickness            float64
	RootRadius                 float64
	DepthBetweenFillets        float64
	EndClearanceForDetailing   float64
	LongitudinalNotchDimension float64
	VerticalNotchDimension     float64
	RadiusOfGyration           RadiusOfGyration
}

type UniversalBeam struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties DimensionsAndProperties
}

type UniversalColumn struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties DimensionsAndProperties
}

type UniversalBearingPile struct {
	SectionClassification   string
	IsNonStandard           bool
	DimensionsAndProperties DimensionsAndProperties
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
