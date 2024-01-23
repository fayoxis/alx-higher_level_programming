#!/usr/bin/python3
""" This program defines a Square class that represents a square."""


class Square:
    """The Square class represents a square."""

    def __init__(self, size=0):
        """
        Initializes a square object.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square
