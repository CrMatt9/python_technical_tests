from src.problem_1.exercise_2 import are_all_digits_different


def test_all_digits_are_different(number_which_all_digits_are_different):
    """
    Test exercise_2.are_all_digits_different
    GIVEN a number which all digits are different
    WHEN validating if all its digits are different
    THEN asserts they are indeed different
    """
    assert are_all_digits_different(number_which_all_digits_are_different)


def test_all_digits_are_not_different(number_with_some_equal_digits):
    """
    Test exercise_2.are_all_digits_different
    GIVEN a number with NOT all digits different
    WHEN validating if all its digits are different
    THEN asserts some of them are duplicated
    """
    assert not are_all_digits_different(number_with_some_equal_digits)
