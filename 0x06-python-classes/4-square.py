#!/usr/bin/python3
"""Class Square that represents a square"""


class Square:
    """Class Square that represents a square"""
    def __init__(self, side_length=0):
        """Initialize the square

        Args:
            side_length (int): Length of the side of the square.
        """
        self.side_length = side_length

    @property
    def side_length(self):
        """int: Length of the side of the square.

        Returns:
            Length of the side of the square.
        """
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        """Set the value as the side length of the square, must be an int.

        Args:
            value (int): Length of the side of the square.
        """
        if type(value) is not int:
            raise TypeError('side_length must be an integer')
        elif value < 0:
            raise ValueError('side_length must be >= 0')
        else:
            self.__side_length = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            Area of the square.
        """
        return self.__side_length ** 2
