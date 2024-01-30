#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix.

Attributes:
    matrix_divided: divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(message)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
