from typing import Generic, TypeVar

from gazelle.steel.sections.abc import (
    SteelSection
)


S = TypeVar("S", bound=SteelSection)


class SteelSections(Generic[S]):
    """A collection of steel sections."""

    def __init__(self, sections: list[S]):
        """Initialise the collection."""
        self.sections = sections

    def __len__(self):
        """Return the number of sections in the collection."""
        return len(self.sections)

    def __getitem__(self, index: int):
        """Return the section at the given index."""
        return self.sections[index]

    def to_json(self):
        """Return a JSON representation of the collection."""
        return {section.designation: section.to_json() for section in self.sections}
