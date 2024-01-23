#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
        Square class that defines a square.

        Private instance attribute:
            - size: the size of the square

        Instantiation:
            __init__(self, size=0)

        Raises:
            - TypeError: if size is not an integer
            - ValueError: if size is less than 0
    """

    def __init__(self, size=0):
        """
        Initializes a new private instance of the Square class.

        Args:
            size (int): the size of the square (default: 0)

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
