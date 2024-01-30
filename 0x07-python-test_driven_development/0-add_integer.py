#!/usr/bin/python3
"""Defines a function add_integer(a, b=98) that adds two integers.

Attributes:
    add_integer: function that adds two integers.
"""
def add_integer(a, b=98):
    """Adds two integer values.

    Args:
        a (int or float): The first integer value.
        b (int or float, optional): The second integer value. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        int: The sum of a and b.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
