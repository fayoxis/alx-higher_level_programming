#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns the number of characters written to a file."""
        return f.write(text)
