#!/usr/bin/python3
"""Defines a function that multiplies all elements of a matrix.

Attributes:
    m_a (matrix)
    m_b (matrix)
"""


def matrix_mul(m_a, m_b):
    """Return: new matrix with the product of m_a and m_b
    Args:
    param1: m_a - a list of lists representing a matrix
    param2: m_b - a list of lists representing a matrix
    Raise: TypeError, ValueError
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, (int, float)))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, (int, float)))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    while len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    reverse_matrix = []
    for i in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        reverse_matrix.append(new_row)

    new_matrix = []
    for irow in m_a:
        new_row = []
        for jcol in reverse_matrix:
            value = 0
            for k in range(len(reverse_matrix[0])):
                value += irow[k] * jcol[k]
            new_row.append(value)
        new_matrix.append(new_row)

    return (new_matrix)
