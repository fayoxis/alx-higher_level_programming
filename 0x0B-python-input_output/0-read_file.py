#!/usr/bin/python3
"""Module that includes the read_file function"""


def read_file(filename=""):
    """Reads a file and outputs its content to the console.

    Args:
        filename (str, optional): The name of the file
        to be read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        file_content = f.read()
        print(file_content, end='')
