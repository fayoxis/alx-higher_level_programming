#!/usr/bin/python3
"""Module function append_write"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number
    of characters.

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: the number of characters appended to file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """
        This block of code opens the file in append mode, writes the text
        to the file, and returns the number of characters appended.
        """
        return f.write(text)
