#!/usr/bin/python3
"""Defines a function called is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class;
    returns True if it is, otherwise False.

    Args:
        obj (a_class): The object to check its type.
        a_class (type): The type of class to check against.

    Returns:
        boolean: True or False.
    """
    return isinstance(obj, a_class)
