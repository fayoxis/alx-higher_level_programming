#!/usr/bin/python3


def max_integer(my_list=None):
    if my_list is None or len(my_list) == 0:
        return None
    return max(my_list)
