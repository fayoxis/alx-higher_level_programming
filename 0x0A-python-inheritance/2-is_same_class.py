#!/usr/bin/python3
"""Defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """Checks if the object is an instance of the specified class.

    Args:
        obj (a_class): The object to check.
        a_class (type): The type of class to compare against.

    Returns:
        bool: True if the object is an instance of the specified
        class; False otherwise.
    """
   return type(obj) == a_class
