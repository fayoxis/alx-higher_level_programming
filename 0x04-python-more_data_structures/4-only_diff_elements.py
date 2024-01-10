#!/usr/bin/python3

def find_symmetric_difference(set_1, set_2):
    symmetric_difference = set_1 ^ set_2
    return {element for element in symmetric_difference if (element in set_1 and element not in set_2) or
            (element in set_2 and element not in set_1)}
