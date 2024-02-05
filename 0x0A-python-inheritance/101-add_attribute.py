#!/usr/bin/python3
"""add_attribute function"""

def add_attribute(obj, attr_name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (__main__.MyClass): The object to which the attribute will be added.
        attr_name ('str'): The name of the attribute.
        value (str): The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
