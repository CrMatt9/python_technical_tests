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
