#!/usr/bin/python3
class Square:
    """This class represents a square."""
    def __init__(self, size=0):
        """Initialize the square class.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size


# Example usage
if __name__ == '__main__':
    square = Square(5)
    print("Area of the square:", square.area())
