
def get_squares() -> list[int]:
    """
    Generate squares of numbers from 1 to 20.

    Returns:
        List of squared integers.
    """
    return list(map(lambda number: number ** 2, range(1, 21)))
