#!/usr/bin/python3
"""Defines a function that prints a given name.

Attributes:
    say_given_name: function that prints a given name.
"""


def say_given_name(given_name, family_name=""):
    """Prints a given name.

    Args:
        given_name (str): The given name.
        family_name (str, optional): The family name. Defaults to "".

    Raises:
        TypeError: If either given name or family name is not a string.

    Prints:
        The name in the format "The name is {given_name} {family_name}".
    """
    if not isinstance(given_name, str):
        raise TypeError("given_name must be a string")

    if not isinstance(family_name, str):
        raise TypeError("family_name must be a string")

    print("The name is {} {}".format(given_name, family_name))
