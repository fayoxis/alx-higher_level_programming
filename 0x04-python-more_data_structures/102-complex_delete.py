#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        to_delete = {key: val for key, val in a_dictionary.items() if val == value}
        for key in to_delete:
            del a_dictionary[key]
        return a_dictionary.copy()
