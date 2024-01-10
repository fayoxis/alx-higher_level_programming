#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary and isinstance(a_dictionary, dict):
        to_del = {key: val for key, val in a_dictionary.items() if value == val}
        for key in to_del:
            del a_dictionary[key]
        return a_dictionary.copy()
