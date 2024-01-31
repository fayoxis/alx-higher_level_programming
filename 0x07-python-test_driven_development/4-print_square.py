#!/usr/bin/python3
"""This script defines a function that prints a square with the character #.

Attributes:
    print_square: A function that prints a square with the character #.
"""


def print_square(size):
    """Return: the n '#' of squares
    Args:
    Param1: Type int the size of the square
    Raises: TypeError and ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    while size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
