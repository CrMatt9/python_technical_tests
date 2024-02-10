import re

import pytest

from src.problem_1.exercise_4 import CustomString


class TestCustomString:
    """Test Custom String class"""

    def test_successfully_create_custom_string(
        self, string_pair_with_only_alpha_characters
    ):
        """
        Test exercise_4.CustomString creation
        GIVEN a pair of strings which only contains alpha characters or spaces
        WHEN instantiating a CustomString class using given strings
        THEN generates a string which is identical to original one
        """
        for s in string_pair_with_only_alpha_characters:
            assert s == CustomString(s)

    def test_warn_and_cleansing_on_custom_string_creation(
        self, string_pair_with_no_alpha_characters
    ):
        """
        Test exercise_4.CustomString creation warning and string cleansing
        GIVEN a pair of strings which contains special or numeric characters
        WHEN instantiating a CustomString class using given strings
        THEN generates a string with only the alpha or spaces characters from the original one, removing all the others,
        and raising a warning specifying which characters have been removed
        """
        with pytest.warns():
            for s in string_pair_with_no_alpha_characters:
                clean_string = CustomString(s)
                assert s != clean_string
                assert bool(re.match("^[a-zA-Z\s]*$", clean_string))

    def test_successfully_add_substring(self, string_pair_with_only_alpha_characters):
        """
        Test exercise_4.CustomString add
        GIVEN a pair of strings which only contains alpha characters or spaces
        WHEN instantiating a CustomString class and concatenating another string
        THEN generates an string which is the sum of both
        """
        string1, string2 = string_pair_with_only_alpha_characters
        s = CustomString(string1) + string2
        assert s == (string1 + string2)

    def test_fail_add_substring(
        self,
        string_pair_with_only_alpha_characters,
        string_pair_with_no_alpha_characters,
    ):
        """
        Test exercise_4.CustomString incorrect addition
        GIVEN a pair of strings which contains special or numeric characters and
        another which only contains alpha characters
        WHEN instantiating a CustomString class with only alpha characters and concatenating
        a string with special characters
        THEN raises a ValueError
        """
        string1, _ = string_pair_with_only_alpha_characters
        string2, _ = string_pair_with_no_alpha_characters
        with pytest.raises(ValueError):
            CustomString(string1) + string2
