#!/usr/bin/python3
"""Module function from_jsonstring"""
import json


def from_json_string(my_str):
    """Converts a JSON string into a Python object.

    Args:
        my_str (strings): The JSON string to convert.

    Returns:
        object: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
