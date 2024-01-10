#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dictionary = a_dictionary.copy()
    new_dictionary[key] = value
    return new_dictionary
