#!/usr/bin/python3


def complex_delete(mya_dictionary, value):
    for k, v in list(mya_dictionary.items()):
        if value == v:
            mya_dictionary.pop(k)
    return mya_dictionary
