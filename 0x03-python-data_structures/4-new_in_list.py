#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if not (0 <= idx < len(my_list)):
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
