#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_elements = {ele for ele in my_list}
    return sum(unique_elements)
