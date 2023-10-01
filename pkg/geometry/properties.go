package geometry

// The geometric cross-sectional depth.
type Depth float64

// The geometric cross-sectional width.
type Width float64

// The geometric cross-sectional length.
type Length float64

// The geometric cross-sectional radius of gyration,
// about both the major (XX) and the minor axes (YY).
type RadiusOfGyration struct {
	XX float64
	YY float64
}
