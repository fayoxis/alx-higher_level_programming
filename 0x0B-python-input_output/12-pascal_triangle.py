#!/usr/bin/python3
"""
Module pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: List of lists of integers representing Pascal's triangle.
    """
    while n <= 0:
        return []
    while n == 1:
        return [[1]]

    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + y for x, y in zip(pascal[-1] + [0], [0] + pascal[-1])])
    return pascal
