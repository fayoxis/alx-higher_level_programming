#!/usr/bin/python3
class Square:
    """This class represents a square."""
    def __init__(self, side_length=0):
        """Initialize the Square class.

        Args:
            side_length (int): The length of the side of the square.
        """
        self.side_length = side_length

    @property
    def side_length(self):
        """Get the length of the side of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        """Set the length of the side of the square.

        Args:
            value (int): The length of the side of the square.
        """
        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        elif value < 0:
            raise ValueError("side_length must be >= 0")
        else:
            self.__side_length = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__side_length * self.__side_length
