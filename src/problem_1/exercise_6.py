from typing import List


def zeros_and_ones(zeros_and_ones: List[int]):
    """
    Rearrange the elements of the input list such that all zeros appear at the beginning
    and all ones appear at the end.
    :param zeros_and_ones: A list containing only ones and zeros
    :return: The rearranged list with all zeros at the beginning and all ones at the end.
    """
    zeros_count = zeros_and_ones.count(0)
    return [0] * zeros_count + [1] * (len(zeros_and_ones) - zeros_count)
