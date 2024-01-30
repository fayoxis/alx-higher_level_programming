#!/usr/bin/python3
"""Module to find the maximum integer in a list
"""


def find_max_integer(lst=[]):
    """Function to find and return the maximum integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(lst) == 0:
        return None
    max_num = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > max_num:
            max_num = lst[i]
        i += 1
    return max_num
