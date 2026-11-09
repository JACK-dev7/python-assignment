
def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    Remove duplicates while preserving original order.

    Args:
        numbers: List of integers.

    Returns:
        A list containing unique values in original order.
    """
    seen = set()
    result = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result
