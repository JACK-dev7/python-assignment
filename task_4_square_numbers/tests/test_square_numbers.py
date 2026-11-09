
from src.square_numbers import get_squares


def test_get_squares():
    expected = [
        1, 4, 9, 16, 25,
        36, 49, 64, 81, 100,
        121, 144, 169, 196, 225,
        256, 289, 324, 361, 400
    ]

    assert get_squares() == expected


def test_squares_count():
    assert len(get_squares()) == 20


def test_first_and_last_square():
    squares = get_squares()

    assert squares[0] == 1
    assert squares[-1] == 400


def test_all_values_are_integers():
    assert all(isinstance(number, int) for number in get_squares())
