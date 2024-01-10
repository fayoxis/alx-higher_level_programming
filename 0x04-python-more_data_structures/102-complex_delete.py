#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary is not None and isinstance(a_dictionary, dict):
        items = list(a_dictionary.items())
        to_del = {key: val for (key, val) in items if value == val}
        for (key, val) in to_del.items():
            del a_dictionary[key]
        return a_dictionary.copy()
