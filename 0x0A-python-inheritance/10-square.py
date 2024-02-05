#!/usr/bin/python3
"""
This script defines a Square class based on the Rectangle class from 9-rectangle.py.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""

import sys
sys.path.append('.')
from typing import Any
from rectangle import Rectangle


class Square(Rectangle):
    """
    This class defines a Square.

    Args:
        Rectangle (Rectangle): The rectangle class.
    """

    def __init__(self, size: int) -> None:
        """
        Initializes instances of the Square class.

        Args:
            size (int): The size of one side of the square.
        """
        super().__init__(size, size)
        self.size = size

    def area(self) -> int:
        """
        Calculates the area of a square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
