from src.problem_1.exercise_1 import is_prime, is_circular_prime


def test_is_prime(prime_number):
    """
    Test exercise_1.is_prime which affects on exercise_1.is_circular_prime.
    GIVEN a prime number
    WHEN validating if number is prime
    THEN asserts it is
    """
    assert is_prime(prime_number)


def test_is_not_prime(not_prime_number):
    """
    Test exercise_1.is_prime which affects on exercise_1.is_circular_prime.
    GIVEN a NOT prime number
    WHEN validating if number is prime
    THEN asserts it is NOT prime
    """
    assert not is_prime(not_prime_number)


# Tests for is_circular_prime function
def test_is_circular_prime(circular_prime_number):
    """
    Test exercise_1.is_circular_prime.
    GIVEN a circular prime number
    WHEN validating if number is circular prime
    THEN asserts it is
    """
    assert is_circular_prime(circular_prime_number)


def test_is_not_circular_prime(not_circular_prime_number):
    """
    Test exercise_1.is_circular_prime.
    GIVEN a NOT circular prime number
    WHEN validating if number is circular prime
    THEN asserts it is NOT circular prime
    """
    assert not is_circular_prime(not_circular_prime_number)
