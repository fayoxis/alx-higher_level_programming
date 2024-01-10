#!/usr/bin/python3

def search_replace(my_list, search, replace):
    result = []
    for ele in my_list:
        if ele != search:
            result.append(ele)
        else:
            result.append(replace)
    return result
