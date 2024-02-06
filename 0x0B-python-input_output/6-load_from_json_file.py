#!/usr/bin/python3
"""
This module contains the function load_from_json_file,
which is used to create an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file.

    Returns:
        object: returns The created object.
    """
    with open(filename, 'r', encoding="utf-8") as g:
        return json.load(g)
