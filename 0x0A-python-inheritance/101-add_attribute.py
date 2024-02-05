#!/usr/bin/python3
"""Funtion of module add_attribute"""


def add_attribute(object, attribute, value):
    """Adds new attribute to an object if it's possible.

    Args:
        object (__main__.MyClass): name of the object.
        attribute ('str): the  name the attribute.
        value (str): the value of the attribute.

    Raises:
        TypeError:  if the object can’t have new attribute.
    """
    # print("object type ---> {}".format(type(object)))
    # print("attr_name type ---> {}".format(type(attr_name)))
    # print("value type ---> {}".format(type(value)))
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
