from gazelle.steel.fabricator import SteelFabricator, SectionCategory

sections = SteelFabricator.make_all_sections(SectionCategory.UC)
for section in sections:
    print(f'Section: {section}, width: {section.width}')