from gazelle.steel import SteelFabricator, SectionCategory

def test_steel():
  sections = SteelFabricator.make_all_sections(SectionCategory.UB)
  assert len(sections) > 0
