#!/usr/bin/python3
"""This script defines a Rectangle class that
inherits from the BaseGeometry class.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        """Creates a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
