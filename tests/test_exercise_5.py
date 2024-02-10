from src.problem_1.exercise_5 import max_subsequence_sum


def test_max_subsequence_sum(list_of_ints_and_ts_max_subsequence_sum):
    """
    Test for the max_subsequence_sum function
    GIVEN a list of integers and the expected maximum subsequence sum
    WHEN the max_subsequence_sum function is called with the given list
    THEN it should return the expected maximum subsequence and its sum
    """
    list_of_ints, expected_result = list_of_ints_and_ts_max_subsequence_sum
    assert max_subsequence_sum(list_of_ints) == expected_result
