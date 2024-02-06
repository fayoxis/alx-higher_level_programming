#!/usr/bin/python3
"""
This module contains the function save_to_json_file, which is
used to write an object to a text file using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj (type): The object to write to the text file.
        filename (str): The name of the file.

    Returns:
        type: The JSON representation.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
