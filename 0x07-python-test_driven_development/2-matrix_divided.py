#!/usr/bin/python3
"""Defines the function that divides all elements of matrix.

Attributes:
    matrix_divided: it divides all elements of matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements in a matrix
    Args:
    param1: matrix type arg of list
    param2: div type int or float
    Return: new matrix with division calculated
    Raise: TypeError, ZeroError
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(element, int) or isinstance(element, float))
                for element in [number for row in matrix for number in row])):

        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    while div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
