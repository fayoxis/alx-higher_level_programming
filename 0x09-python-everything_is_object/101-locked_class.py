#!/usr/bin/python3
"""Defines a restricted class."""


class RestrictedClass:
    """
    Restricts the user from creating new attributes in RestrictedClass
    except for attributes named 'first_name'.
    """

    __slots__ = ["first_name"]
