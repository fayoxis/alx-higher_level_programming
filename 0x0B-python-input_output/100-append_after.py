#!/usr/bin/python3
"""Module append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each line,
    containing a specific string.
    """
    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as fo:
        save = ""
        for line in text:
            save += line
            while search_string in line:
                save += new_string
        fo.write(save)
