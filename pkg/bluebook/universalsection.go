package bluebook

import (
	units "github.com/GazelleKit/gazelle/pkg/units"
)

type DimensionsAndProperties struct {
	Depth                      units.Millimetre
	Width                      units.Millimetre
	Length                     units.Millimetre
	TotalMass                  units.Kilogram
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
