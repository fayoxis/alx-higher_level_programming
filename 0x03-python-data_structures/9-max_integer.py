#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    max_value = float('-inf')
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
