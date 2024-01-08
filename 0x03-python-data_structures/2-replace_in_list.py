#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    list_len = len(my_list)
    if idx < 0 or idx >= list_len:
        return my_list

    my_list[idx] = element
    return my_list
