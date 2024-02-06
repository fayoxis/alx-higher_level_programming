#!/usr/bin/python3
"""
This script defines the function class_to_json, which
converts an object into a dictionary
representation suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary description with a simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj (MyClass): The object.

    Returns:
        dict: The dictionary.
    """
    return obj.__dict__
