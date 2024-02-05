#!/usr/bin/python3
"""
This script defines a class called Square, which is based
on the Rectangle class from the module 9-rectangle.py.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""

# Import the Rectangle class from the module 9-rectangle.py
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    This class defines a square.

    Args:
        Rectangle (Rectangle): The base class of the square.

    Attributes:
        size (int): The size of one side of the square.
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

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
