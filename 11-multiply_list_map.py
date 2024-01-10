#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiplied_list = list(map(lambda x: x * number, my_list))
    return multiplied_list
