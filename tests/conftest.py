import pytest

some_circular_prime_numbers = [
    2,
    5,
    11,
    37,
    113,
    197,
    199,
    337,
    1193,
    3779,
    11939,
    19937,
    193939,
    199933,
]

some_not_circular_prime_numbers_but_primes = [41, 53, 59, 61, 67, 83, 89]

some_prime_numbers = {
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
}

some_not_prime_numbers = [
    n for n in range(max(some_prime_numbers)) if n not in some_prime_numbers
]

some_numbers_with_some_equal_digits = some_circular_prime_numbers[-8:]

some_numbers_which_all_digits_are_different = [
    12345,
    2548,
    65478,
    12369,
    9856,
    145789,
    2,
    48,
    0,
    6587123,
]


@pytest.fixture(scope="session", params=some_circular_prime_numbers)
def circular_prime_number(request):
    return request.param


@pytest.fixture(scope="session", params=some_prime_numbers)
def prime_number(request):
    return request.param


@pytest.fixture(
    scope="session",
    params=some_not_prime_numbers,
)
def not_prime_number(request):
    return request.param


@pytest.fixture(
    scope="session",
    params=some_not_circular_prime_numbers_but_primes + some_not_prime_numbers,
)
def not_circular_prime_number(request):
    return request.param


@pytest.fixture(
    scope="session",
    params=some_numbers_which_all_digits_are_different,
)
def number_which_all_digits_are_different(request):
    return request.param


@pytest.fixture(
    scope="session",
    params=some_numbers_with_some_equal_digits,
)
def number_with_some_equal_digits(request):
    return request.param

some_pairs_of_numbers_and_its_mod9 = [(69810, 6), (3201, 6), (89822, 2), (84135, 3), (54571,4)]
@pytest.fixture(
    scope="session",
    params=some_pairs_of_numbers_and_its_mod9,
)
def pair_of_number_and_its_mod9(request):
    return request.param
