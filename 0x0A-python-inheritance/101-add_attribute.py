#!/usr/bin/python3
"""add_attribute Function"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr_name: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add new attribute")
    setattr(obj, attribute, value)
