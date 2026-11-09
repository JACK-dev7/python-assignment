
from src.remove_duplicates import remove_duplicates


def test_remove_duplicates():
    numbers = [4, 2, 5, 2, 4, 7, 5, 8]

    assert remove_duplicates(numbers) == [4, 2, 5, 7, 8]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_list_without_duplicates():
    numbers = [1, 2, 3, 4]

    assert remove_duplicates(numbers) == [1, 2, 3, 4]


def test_all_elements_are_duplicates():
    numbers = [5, 5, 5, 5]

    assert remove_duplicates(numbers) == [5]


def test_preserve_original_order():
    numbers = [9, 3, 7, 3, 1, 9, 5]

    assert remove_duplicates(numbers) == [9, 3, 7, 1, 5]
