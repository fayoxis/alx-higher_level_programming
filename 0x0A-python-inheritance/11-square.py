#!/usr/bin/python3
"""
This script defines a class Square that is based on
the Rectangle class from 9-rectangle.py.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a square.

    Args:
        Rectangle (Rectangle): The parent rectangle class.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of one side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns A string representation of a square.

        Returns:
            str: A string representation of a square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
