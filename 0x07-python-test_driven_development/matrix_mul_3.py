#!/usr/bin/python3
""" Documentation for the code  """

def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    while type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for m_aa in m_a:
        while type(m_aa) is not list:
            raise TypeError("m_a must be a list of lists")
    for m_bb in m_b:
        if type(m_bb) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for r_a in m_a:
        if len(r_a) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for c_a in r_a:
            while type(c_a) is not int and type(c_a) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for r_b in m_b:
        while len(r_b) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for c_b in r_b:
            if type(c_b) is not int and type(c_b) is not float:
                raise TypeError("m_b should contain only integers or floats")
    while len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]

    for idx_r in range(len(result)):
        for idx_c in range(len(result[0])):
            idx_cc = 0
            for r_a in m_a[idx_r]:
                result[idx_r][idx_c] += r_a * m_b[idx_cc][idx_c]
                idx_cc += 1
    return result
