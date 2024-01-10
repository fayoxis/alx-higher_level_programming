#!/usr/bin/python3


def complex_delete(my_dict, value):
    for k, v in list(my_dict.items()):
        if value == v:
            my_dict.pop(k)
    return my_dict
