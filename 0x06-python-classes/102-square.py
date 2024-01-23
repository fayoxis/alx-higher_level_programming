#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class that defines a square"""

    def __init__(self, size: int = 0):
        """Initialize the square.

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self) -> int:
        """int: Private size of the square.

        Returns:
            The private size of the square.
        """
        return self.__size

    @size.setter
    def size(self, new_size: int):
        """Set the size of the square.

        Args:
            new_size (int): Size of the square.
        """
        if not isinstance(new_size, int):
            raise TypeError('size must be an integer')
        elif new_size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = new_size

    def area(self) -> int:
        """Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other) -> bool:
      
        return self.size < other.size

    def __le__(self, other) -> bool:
      
        return self.size <= other.size

    def __eq__(self, other) -> bool:
   
        return self.size == other.size

    def __ne__(self, other) -> bool:
    
        return self.size != other.size

    def __ge__(self, other) -> bool:
        return self.size >= other.size
