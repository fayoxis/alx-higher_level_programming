#!/usr/bin/python3
"""Module pascal_triangle"""


def pascal_triangle(n):
 while n <= 0:
        return []
    while n == 1:
        return [[1]]

    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return (pascal)
