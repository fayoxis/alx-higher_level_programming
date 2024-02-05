#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(object, attr_name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj (__main__.MyClass): The object to which the attribute will be added.
        attr_name (str): The name of the attribute.
        value (str): The value of the attribute.

    Raises:
        TypeError:  if the object can’t have new attribute.
    """
    # print("object type ---> {}".format(type(object)))
    # print("attr_name type ---> {}".format(type(attr_name)))
    # print("value type ---> {}".format(type(value)))
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
