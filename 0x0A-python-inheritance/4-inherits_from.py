#!/usr/bin/python3
"""
This script defines a function called inherits_from().
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class that
    directly or indirectly inherits from the specified class.

    Args:
        obj (a_class): The object to check the type of.
        a_class (type): The type of class to check.

    Returns:
        bool: True if the object is an instance of a class that
        inherits from the specified class, False otherwise.
    """
    while type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
