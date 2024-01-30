#!/usr/bin/python3
import math
"""
Defines a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The value to divide each element of the matrix by.

    Raises:
        TypeError: If the matrix is not a matrix (list of lists) of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If an element of any list is not an integer or float.
        TypeError: If a row in the matrix is not a list.
        TypeError: If the divisor is not an integer or a float.
        ZeroDivisionError: If the divisor is equal to 0.

    Returns:
        list: A new matrix with the result of dividing each element by the divisor.
    """
    message = "The matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(message)

    if not isinstance(div, (int, float)):
        raise TypeError("The divisor must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
