package units

type Gram float64
type Kilogram float64

type Metre float64
type Millimetre float64

type Length interface {
	Metre | Millimetre
}

type Mass interface {
	Gram | Kilogram
}

type Volume[L Length] float64
type Density[M Mass, V Volume[L], L Length] float64

func (g Gram) ToKilogram() Kilogram {
	return Kilogram(g / 1000.0)
}

func (kg Kilogram) ToGram() Gram {
	return Gram(kg * 1000.0)
}

func (g Gram) ToDensity(v Volume[Metre]) Density[Gram, Volume[Metre], Metre] {
	return Density[Gram, Volume[Metre], Metre](float64(g) / float64(v))
}

func (kg Kilogram) ToDensity(v Volume[Metre]) Density[Kilogram, Volume[Metre], Metre] {
	return Density[Kilogram, Volume[Metre], Metre](float64(kg) / float64(v))
}

func Go() Density[Gram, Volume[Metre], Metre] {
	m := Gram(1)
	l := Metre(1)
	v := Volume[Metre](float64(m) * float64(l))
	d := m.ToDensity(v)
	return d
}
