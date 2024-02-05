#!/usr/bin/python3
"""Defines the function is_same_class()"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the
    specified class, and False otherwise.

    Args:
        obj (a_class): Object to check the type of.
        a_class (type): Type of class to check.

    Returns:
      bool: True if the object is an instance of the
      specified class; False otherwise.
    """
    return type(obj) == a_class
