#!/usr/bin/python3
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
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If an element of any list is not an integer or float.
        TypeError: If a row in the matrix is not a list.
        TypeError: If the divisor is not an integer or a float.
        ZeroDivisionError: If the divisor is equal to 0.

    Returns:
        list: A new matrix with the result of dividing each element by the divisor.
    """
    row_size = None
    message = "The matrix must be a matrix (list of lists) of integers/floats"

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
        raise TypeError("The divisor must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix

# Example usage
matrix = [[1, 2, 3], [4, 5, 6]]
divisor = 3
result = matrix_divided(matrix, divisor)
print(result)
