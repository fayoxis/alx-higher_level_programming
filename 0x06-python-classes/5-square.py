#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0):
        """Initialize square

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: Private size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size, must be an integer.

        Args:
            value (int): Size of the square.
        """
        if type(value) is not int:
            raise TypeError('Size must be an integer')
        elif value < 0:
            raise ValueError('Size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square.

        Returns:
            Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout."""

        if self.__size != 0:
            for _ in range(self.__size):
                print('#' * self.__size)
        else:
            print()
