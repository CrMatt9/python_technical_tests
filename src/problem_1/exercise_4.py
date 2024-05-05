import warnings
from typing import List


class CustomString(str):
    """
    >>> string1 = CustomString("Ho,la")
    Warning
    The created instance can only contain characters from "a" to "z".'
    The characters [","] will be removed."
    >>> string1 + ","
    Except ValueError
    Cannot add non-alphabetic characters to CustomString.
    >>> string1 + " mundo"
    >>Hola mundo
    """

    def __new__(cls, value: str, verbose=True):
        clean_value = cls._clean_string(value)
        invalid_characters = cls._get_invalid_characters(
            value=value, clean_value=clean_value
        )
        if invalid_characters and verbose:
            warnings.warn(
                f'The created instance can only contain characters from "a" to "z". The characters '
                f"{invalid_characters} will be removed."
            )
        return super().__new__(cls, clean_value)

    def __add__(self, other: str) -> "CustomString":
        cleaned_other = self._clean_string(other)
        invalid_characters = self._get_invalid_characters(
            value=other,
            clean_value=cleaned_other,
        )
        if invalid_characters:
            raise ValueError("Cannot add non-alphabetic characters to CustomString.")
        return CustomString(super().__add__(other))

    @staticmethod
    def _get_invalid_characters(value: str, clean_value: str) -> List[str]:
        """
        Gather all invalid characters from a string
        :param value: Raw string which may contain some invalid characters
        :param clean_value: Cleaned string where all invalid characters have been filtered out
        :return: List of invalid characters between double quotes
        """
        invalid_characters = set(value).difference(set(clean_value))
        return [
            '"' + str(invalid_character) + '"'
            for invalid_character in invalid_characters
        ]

    @staticmethod
    def _clean_string(value: str) -> str:
        """
        Removes characters which are not alpha or spaces from string
        :param value: Raw string which may contain some invalid characters
        :return: Cleaned string
        """
        return "".join(char for char in value if char.isalpha() or char.isspace())
