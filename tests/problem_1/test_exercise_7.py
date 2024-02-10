import pytest

from problem_1.conftest import (
    some_computer_params,
    some_desktop_params,
    some_laptop_params,
)
from src.problem_1.exercise_7 import Desktop, Laptop, Computer


@pytest.mark.parametrize(
    "brand, model, expected_str",
    some_computer_params,
)
def test_computer_str(brand, model, expected_str):
    """
    Test exercise_7.Computer string representation
    GIVEN a Computer object with a specific brand and model,
    WHEN converting the object to a string,
    THEN the string representation should match the expected string.
    """
    computer = Computer(brand, model)
    assert str(computer) == expected_str


@pytest.mark.parametrize(
    "brand, model, cpu_volume, expected_str",
    some_desktop_params,
)
def test_desktop_str(brand, model, cpu_volume, expected_str):
    """
    Test exercise_7.Desktop string representation
    GIVEN a Desktop object with a specific brand, model, and CPU volume,
    WHEN converting the object to a string,
    THEN the string representation should match the expected string.
    """
    desktop = Desktop(brand, model, cpu_volume)
    assert str(desktop) == expected_str


@pytest.mark.parametrize(
    "brand, model, battery_duration, expected_str",
    some_laptop_params,
)
def test_laptop_str(brand, model, battery_duration, expected_str):
    """
    Test exercise_7.Laptop string representation
    GIVEN a Laptop object with a specific brand, model, and battery duration,
    WHEN converting the object to a string,
    THEN the string representation should match the expected string.
    """
    laptop = Laptop(brand, model, battery_duration)
    assert str(laptop) == expected_str
