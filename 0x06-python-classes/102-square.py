#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: Private size of the square.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): Size of the square.
        """
        if type(value) is not int or type(value) is not float:
            raise TypeError('Size must be a number')
        elif value < 0:
            raise ValueError('Size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size**2

    def __lt__(self, other):
        """Check if the size of the current square is
        less than the size of another square.

        Args:
            other (Square): Another square object.

        Returns:
            True if the current square is smaller, False otherwise.
        """
        return self.size < other.size

    def __le__(self, other):
        """Check if the size of the current square is less
        than or equal to the size of another square.

        Args:
            other (Square): Another square object.

        Returns:
            True if the current square is smaller or equal, False otherwise.
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Check if the size of the current square is equal to the size of another square.

        Args:
            other (Square): Another square object.

        Returns:
            True if the squares are equal in size, False otherwise.
        """
        return self.size == other.size

    def __ne__(self, other):
        """Check if the size of the current square is
        not equal to the size of another square.

        Args:
            other (Square): Another square object.

        Returns:
            True if the squares are not equal in size, False otherwise.
        """
        return self.size != other.size

    def __ge__(self, other):
        """Check if the size of the current square is
        greater than or equal to the size of another square.

        Args:
            other (Square): Another square object.

        Returns:
            True if the current square is larger or equal, False otherwise.
        """
        return self.size >= other.size
