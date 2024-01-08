#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        reversed_list = my_list.copy()
        reversed_list.reverse()
        for i in range(len(reversed_list)):
            print("{:d}".format(reversed_list[i]))
