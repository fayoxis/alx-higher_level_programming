#!/usr/bin/python3
"""module add_attribute"""


def add_attribute(obj, attributes, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attributes: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("The object does not support adding new attributes")
    setattr(obj, attributes, value)
