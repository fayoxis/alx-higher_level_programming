#!/usr/bin/python3
"""Module function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) && returns the number
    of characters.

    Args:
        filename (str, optional): the name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: the number o characters to file.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
