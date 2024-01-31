#!/usr/bin/python3
import math
"""Defines the function that divides all elements of matrix.

Attributes:
    matrix_divided: it divides all elements of matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix.

    Args:
        matrix (list): it is a list of lists of integers or floats.
        div (int/float): it is Value to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers || floats.
        TypeError: If each row of the matrix isn't same size.
        TypeError: If an element of any list is not an integer || float.
        TypeError: If a row in the matrix is not the list.
        TypeError: If div is not an integer || a float.
        ZeroDivisionError: If div is equal to zero.

    Returns:
        matrix: A result of a division.
    """
  if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(element, int) or isinstance(element, float))
                for element in [number for row in matrix for number in row])):

        raise TypeError("matrix must be matrix (list - lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    while div == 0:
        raise ZeroDivisionError("division by 0")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
