#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
     """A class representing a rectangle inheriting from BaseGeometry."""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
