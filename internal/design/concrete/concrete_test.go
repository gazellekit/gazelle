package concrete

import (
	"testing"
)

func TestConcreteName(t *testing.T) {
	if Name != "Concrete" {
		t.Errorf("Name = %s; want Concrete", Name)
	}
}
