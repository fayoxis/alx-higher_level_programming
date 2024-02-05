#!/usr/bin/python3
"""
This script defines a class Rectangle that
inherits from the BaseGeometry class.
It has two attributes:
    - width (int): the width of the rectangle.
    - height (int): the height of the rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    This class represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
