#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for x in row:
            squared_row.append(x ** 2)
        squared_matrix.append(squared_row)
    return squared_matrix
