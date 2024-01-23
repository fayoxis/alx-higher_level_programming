#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class that defines a square"""
    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: Private size of the square.

        Returns:
            The private size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): Size of the square.
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

    def __lt__(self, other):
        """Compare the size of two squares.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the size of the current square is less than the other square, False otherwise.
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare the size of two squares.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the size of the current square is less than or equal to the other square, False otherwise.
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare the size of two squares.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the size of the current square is equal to the other square, False otherwise.
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare the size of two squares.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the size of the current square is not equal to the other square, False otherwise.
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare the size of two squares.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the size of the current square is greater than or equal to the other square, False otherwise.
        """
        return self.size >= other.size
