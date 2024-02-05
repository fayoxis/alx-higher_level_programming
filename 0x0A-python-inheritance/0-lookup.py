#!/usr/bin/python3
"""
Defines a function called lookup
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (class): The object.

    Returns:
        list: The list of available attributes and methods of the object.
    """
    return dir(obj)
