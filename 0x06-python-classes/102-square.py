#!/usr/bin/python3
""" 
This is the Square class that defines a square.
"""


class Square:
    """ 
    This class defines a square.
    """
    def __init__(self, size=0):
        """ 
        Initializes an instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ 
        Sets the size of the square.

        Args:
            value (int): The size of the square.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ 
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def __lt__(self, other):
        """ 
        Checks if the size of the current square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the current square is smaller, False otherwise.
        """
        return self.size < other.size

    def __le__(self, other):
        """ 
        Checks if the size of the current square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the current square is smaller or equal, False otherwise.
        """
        return self.size <= other.size

    def __eq__(self, other):
        """ 
        Checks if the size of the current square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the current square is equal, False otherwise.
        """
        return self.size == other.size

    def __ne__(self, other):
        """ 
        Checks if the size of the current square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the current square is not equal, False otherwise.
        """
        return self.size != other.size

    def __ge__(self, other):
        """ 
        Checks if the size of the current square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if the current square
        """
        return self.size >= other.size
