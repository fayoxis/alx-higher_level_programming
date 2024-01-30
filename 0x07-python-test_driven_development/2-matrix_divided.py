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
    row_size = None
    message = "matrix should be a matrix of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(message)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(message)

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
