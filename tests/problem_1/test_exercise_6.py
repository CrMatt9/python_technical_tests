from src.problem_1.exercise_6 import zeros_and_ones


def test_zeros_and_ones(list_zeros_and_ones):
    """
    Test exercise_6.zeros_and_ones
    GIVEN a list of ones and zeros
    WHEN the zeros_and_ones function is called with the given list
    THEN it should return the rearranged list with all zeros at the beginning and all ones at the end.
    """
    arr, expected_result = list_zeros_and_ones
    assert zeros_and_ones(arr) == expected_result
