from src.problem_1.exercise_3 import add_mod_9_to_the_beginning_of_number


def test_add_mod_9_to_the_beginning_of_number(pair_of_number_and_its_mod9):
    """
    Test exercise_3.add_mod_9_to_the_beginning_of_number
    GIVEN a number greater than 100
    WHEN summing all its digits recursively till the result is between 0 and 9 and concatenate left the result
    to the original number
    THEN assert the result is equal than the expected
    """
    assert add_mod_9_to_the_beginning_of_number(pair_of_number_and_its_mod9[0]) == int(
        str(pair_of_number_and_its_mod9[1]) + str(pair_of_number_and_its_mod9[0])
    )
