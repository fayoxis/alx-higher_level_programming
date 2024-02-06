#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation.

    Args:
        my_obj (type): Object to write to text file.
        filename (str): name of the file.

    Returns:
        type: JSON representation.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
