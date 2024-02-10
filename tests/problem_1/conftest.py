import pytest

from src.problem_1.exercise_8 import User

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

some_string_pairs_with_only_alpha_characters = [
    ("Hello", "this"),
    ("is", "my"),
    ("super cool test", "enjoy"),
]
some_pairs_string_with_no_alpha_characters = [
    ("He5l#lo1", "t.his"),
    ("is,", "m9y"),
    ("supe123r co$%#ol test", "enjoy!"),
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


some_pairs_of_numbers_and_its_mod9 = [
    (69810, 6),
    (3201, 6),
    (89822, 2),
    (84135, 3),
    (54571, 4),
]


@pytest.fixture(
    scope="session",
    params=some_pairs_of_numbers_and_its_mod9,
)
def pair_of_number_and_its_mod9(request):
    return request.param


@pytest.fixture(
    scope="class",
    params=some_string_pairs_with_only_alpha_characters,
)
def string_pair_with_only_alpha_characters(request):
    return request.param


@pytest.fixture(
    scope="class",
    params=some_pairs_string_with_no_alpha_characters,
)
def string_pair_with_no_alpha_characters(request):
    return request.param


some_lists_of_ints_and_its_max_subsequence_sum = [
    ([1, 2, 3, 4], ([1, 2, 3, 4], 10)),
    ([-1, -2, -3, -4], ([], 0)),
    ([-8, -4, 6, 8, -6, 10, -4, -4], ([6, 8, -6, 10], 18)),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], ([4, -1, 2, 1], 6)),
]


@pytest.fixture(
    scope="session",
    params=some_lists_of_ints_and_its_max_subsequence_sum,
)
def list_of_ints_and_ts_max_subsequence_sum(request):
    return request.param


some_lists_zeros_and_ones = [
    ([0, 1, 1, 1, 0], [0, 0, 1, 1, 1]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([1, 0, 1, 0, 1], [0, 0, 1, 1, 1]),
    ([0, 0, 1, 1, 0], [0, 0, 0, 1, 1]),
    ([1, 1, 0, 0, 1], [0, 0, 1, 1, 1]),
    ([0, 1, 0, 1, 0], [0, 0, 0, 1, 1]),
    ([1, 0, 1, 0, 0], [0, 0, 0, 1, 1]),
]


@pytest.fixture(
    scope="session",
    params=some_lists_zeros_and_ones,
)
def list_zeros_and_ones(request):
    return request.param


some_computer_params = [
    ("Dell", "Power", "Brand: Dell, Model: Power"),
    ("HP", "Gaming", "Brand: HP, Model: Gaming"),
    ("Asus", "ZenBook", "Brand: Asus, Model: ZenBook"),
    ("Lenovo", "ThinkPad", "Brand: Lenovo, Model: ThinkPad"),
    ("Acer", "Swift", "Brand: Acer, Model: Swift"),
]


some_desktop_params = [
    ("Dell", "Power", 10, "Brand: Dell, Model: Power, CPU Volume: 10 L"),
    ("HP", "Gaming", 15, "Brand: HP, Model: Gaming, CPU Volume: 15 L"),
    ("Asus", "ZenBook", 8, "Brand: Asus, Model: ZenBook, CPU Volume: 8 L"),
    ("Lenovo", "ThinkPad", 12, "Brand: Lenovo, Model: ThinkPad, CPU Volume: 12 L"),
    ("Acer", "Swift", 6, "Brand: Acer, Model: Swift, CPU Volume: 6 L"),
]


some_laptop_params = [
    ("Dell", "Mini Power", 2, "Brand: Dell, Model: Mini Power, Battery Duration: 2 h"),
    ("HP", "UltraBook", 5, "Brand: HP, Model: UltraBook, Battery Duration: 5 h"),
    ("Asus", "ZenBook", 8, "Brand: Asus, Model: ZenBook, Battery Duration: 8 h"),
    (
        "Lenovo",
        "ThinkPad",
        12,
        "Brand: Lenovo, Model: ThinkPad, Battery Duration: 12 h",
    ),
    ("Acer", "Swift", 6, "Brand: Acer, Model: Swift, Battery Duration: 6 h"),
]


@pytest.fixture(
    scope="function",
)
def setup_users_database():
    User._total_users = 0
    yield
    User._total_users = 0


@pytest.fixture(
    scope="function",
)
def tmp_directory(tmpdir):
    return tmpdir.mkdir("test_files")
