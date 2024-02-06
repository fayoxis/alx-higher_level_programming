#!/usr/bin/python3
"""
This module contains a function called to _jsonstring.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a string object.

    Args:
        my_obj (object): The object to examine.

    Returns:
        str: The JSON representation of the object.
    """

    # Serializing to JSON
    return json.dumps(my_obj)
