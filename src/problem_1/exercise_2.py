def are_all_digits_different(number: int) -> bool:
    """
    Checks if all digits are different
    :param number: Integer number
    :return: Weather the number introduces has all digits different
    """
    number_str = str(number)
    return len(number_str) == len(set(number_str))
