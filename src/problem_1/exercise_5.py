from typing import List


def max_subsequence_sum(list_of_ints: List[int]):
    """
    Find the maximum subsequence sum and the corresponding subsequence in the given list of numbers.
    :param list_of_ints: (list of int): A list of integers.
    :return: A tuple containing the maximum subsequence and its sum.

    >>> max_subsequence_sum([-8, -4, 6, 8, -6, 10,-4,-4])
    ([6, 8, -6, 10], 18)
    """
    max_sum = 0
    current_sum = 0
    start_index = end_index = current_start_index = 0

    for i, num in enumerate(list_of_ints):
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start_index
            end_index = i + 1

        if current_sum <= 0:
            current_sum = 0
            current_start_index = i + 1

    return list_of_ints[start_index:end_index], max_sum
