#!/usr/bin/python3
"""Defines a class Square based on the Rectangle class.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


from typing import Union


class Rectangle:
    """Defines a class Rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width: int, height: int):
        """Creates new instances of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> int:
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self) -> str:
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"


class Square(Rectangle):
    """Defines a class Square.

    Args:
        Rectangle (Rectangle): The base rectangle class.
    """

    def __init__(self, size: int):
        """Creates new instances of the Square class.

        Args:
            size (int): The size of one side of the square.
        """
        super().__init__(size, size)
        self.size = size

    def area(self) -> int:
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
