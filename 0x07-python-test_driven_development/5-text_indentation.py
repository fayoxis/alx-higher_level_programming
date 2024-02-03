#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each occurrence of the characters '.', '?', and ':'.

Attributes:
    text_indentation: A function that prints a text with specific conditions.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after encountering
    '.', '?', or ':' characters.

    Args:
        text (str): The input string to be examined.

    Raises:
        TypeError: If text is not of type str.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
