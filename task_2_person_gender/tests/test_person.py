
import pytest

from src.person import Female, Male, Person


def test_male_get_gender():
    male = Male()
    assert male.get_gender() == "Male"


def test_female_get_gender():
    female = Female()
    assert female.get_gender() == "Female"


def test_person_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Person()


def test_incomplete_subclass_cannot_be_instantiated():
    class IncompletePerson(Person):
        pass

    with pytest.raises(TypeError):
        IncompletePerson()
