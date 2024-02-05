#!/usr/bin/python3
"""add_attribute function"""

def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attribute: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add new attribute to object")
    setattr(obj, attribute, value)
