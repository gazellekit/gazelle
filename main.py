from gazelle.steel import SectionCategory, SteelFabricator

sections = SteelFabricator.make_all_sections(SectionCategory.UB)

for section in sections:
  print(section)
