#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices by using the module NumPy.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    # m_a = ([1, 2], [3, 4])
    # m_b = [[1, 2], [3, 4]]
    return np.matmul(m_a, m_b)
