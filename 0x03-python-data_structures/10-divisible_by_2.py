#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return None

    bool_list = [my_list[i] % 2 == 0 for i in range(list_len)]
    return bool_list
