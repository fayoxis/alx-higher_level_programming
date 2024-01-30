#!/usr/bin/python3
"""Defines a function that prints my name.

Attributes:
    say_my_name: function that prints my name.
"""


def say_my_name(first_name, last_name=""):
    """Prints a given name.

    Args:
        given_name (str): The given name.
        family_name (str, optional): The family name. Defaults to "".

    Raises:
        TypeError: If either given name or family name is not a string.

    Prints:
        The name in the format "The name is {given_name} {family_name}".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
