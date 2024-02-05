#!/usr/bin/python3
"""Funtion add_attribute"""


def add_attribute(object, attr_name, value):

    # print("object type ---> {}".format(type(object)))
    # print("attr_name type ---> {}".format(type(attr_name)))
    # print("value type ---> {}".format(type(value)))
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
