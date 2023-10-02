package bluebook

import (
	units "github.com/calcpadstudio/gazelle/pkg/units"
	"golang.org/x/exp/constraints"
)

type DimensionsAndProperties[L units.Length[T], M units.Mass[T], T constraints.Float] struct {
	Depth                      L
	Width                      L
	Length                     L
	TotalMass                  M
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
	RadiusOfGyration           float64
}
