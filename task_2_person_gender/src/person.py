
from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class representing a person."""

    @abstractmethod
    def get_gender(self) -> str:
        """Return the gender of the person."""
        pass


class Male(Person):
    """Represents a male person."""

    def get_gender(self) -> str:
        return "Male"


class Female(Person):
    """Represents a female person."""

    def get_gender(self) -> str:
        return "Female"
