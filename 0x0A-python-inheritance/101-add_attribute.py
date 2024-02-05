#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (__main__.MyClass): The object to add the attribute to.
        attr_name ('str'): The name of the attribute.
        value (str): The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    # print("object type ---> {}".format(type(obj)))
    # print("attr_name type ---> {}".format(type(attr_name)))
    # print("value type ---> {}".format(type(value)))
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add new attribute")
    setattr(obj, attr_name, value)
