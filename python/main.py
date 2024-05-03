import gazelle as gz
from .steel import SteelFabricator, SectionCategory, UniversalBeam

print("Welcome to Gazelle! 🦌")
print(f'The answer is: {gz.sum_as_string(10, 32)}')

sections = SteelFabricator[UniversalBeam] \
  .make_all_sections(SectionCategory.UB)

for section in sections:
  print(section)
