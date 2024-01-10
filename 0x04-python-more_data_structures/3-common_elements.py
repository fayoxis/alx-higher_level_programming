#!/usr/bin/python3


def uniq_add(my_list=None):
    if my_list is None:
        my_list = []
    return sum({ele for ele in my_list})
