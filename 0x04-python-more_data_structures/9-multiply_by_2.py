#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiplied_dictionary = {}
    for key, value in a_dictionary.items():
        multiplied_dictionary[key] = value * 2
    return multiplied_dictionary
