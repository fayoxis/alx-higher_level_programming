#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    multiplied_list = []
    for n in my_list:
        multiplied_list.append(n * number)
    return multiplied_list
