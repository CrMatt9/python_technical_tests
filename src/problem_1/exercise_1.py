"""
EXERCISE STATEMENT:
Escribir una función que, dado un entero positivo devuelva True si el número es un primo
circular y False en otro caso.
Nota: Un número es primo circular si es un número primo y todas las rotaciones de sus dígitos
son números primos también. Por ejemplo: 197 lo es ya que 197, 971 y 719 son números primos.
"""
from math import isqrt


def is_prime(n: int) -> bool:
    """
    Checks if a given number is prime or not
    :param n: Integer number to evaluate
    :return: Whether the given number is prime or not
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_circular_prime(number: int) -> bool:
    """
    Checks if a given number is circular prime or not
    :param number: Integer number to evaluate
    :return: Whether the given number is circular prime or not
    """
    # Extract first primes and circular prime numbers to generalize logic
    if number in {2, 3, 5}:
        return True
    number_str = str(number)
    split_number_list = [int(i) for i in number_str]
    # If number contains a 5, any number pair or the sum of the digits is divisible per 3, it cannot be circular prime
    if (
        any([n % 2 == 0 or n == 5 for n in split_number_list])
        or sum(split_number_list) % 3 == 0
    ):
        return False
    # Check all combinations if any is not prime it cannot be circular prime therefore we exit on the first not prime
    for i in range(len(number_str)):
        if not is_prime(int(number_str[i:] + number_str[:i])):
            return False
    return True
