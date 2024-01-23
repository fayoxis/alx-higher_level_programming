#!/usr/bin/python3
"""Class Square that represents a square."""


class Square:
    """Class Square that represents a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """int: The size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
