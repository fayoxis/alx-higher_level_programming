#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i != len(row) - 1:
                endCh = ' '
            else:
                endCh = ''
            print("{:d}".format(num), end=endCh)
        print("")
