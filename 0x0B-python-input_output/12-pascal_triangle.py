#!/usr/bin/python3
"""Module pascal_triangle"""


def pascal_triangle(n):
    while n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for i in range(n - 1):
        row = [x + y for x, y in zip(triangle[-1] + [0], [0] + triangle[-1])]
        triangle.append(row)

    return triangle
