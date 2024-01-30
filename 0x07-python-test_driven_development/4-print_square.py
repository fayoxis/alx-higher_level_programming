#!/usr/bin/python3
"""This script defines a function that prints a square with the character #.

Attributes:
    print_square: A function that prints a square with the character #.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size of the square (length of one side).

    Raises:
        TypeError: If size is not an integer or is less than 0.
        ValueError: If size is less than 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
