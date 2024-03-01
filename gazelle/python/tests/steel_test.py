from ..src.steel import SectionCategory, SteelFabricator


def test_steel():
  sections = SteelFabricator.make_all_sections(SectionCategory.UB)
  assert len(sections) > 0
