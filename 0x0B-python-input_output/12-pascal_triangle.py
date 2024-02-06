#!/usr/bin/python3
"""Module pascal_triangle"""


def pascal_triangle(n):
    """Returns list of lists of integers of the Pascal’s,
    triangle of n.

    Args:
        n (int): it is the rows of triangle.

    Returns:
        list: return lists of lists of integers.
    """
    while n <= 0:
        return []
    while n == 1:
        return [[1]]

    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return (pascal)
