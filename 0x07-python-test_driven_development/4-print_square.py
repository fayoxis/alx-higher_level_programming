#!/usr/bin/python3
"""Defines a function that prints a square with the character #.

Attributes:
    print_square: function that prints a square with the character #.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size of the square (1 side).

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
