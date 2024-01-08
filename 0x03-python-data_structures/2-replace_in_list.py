#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_len = len(my_list)
    if not (0 <= idx < list_len):
        return my_list

    updated_list = my_list.copy()
    updated_list[idx] = element
    return updated_list
