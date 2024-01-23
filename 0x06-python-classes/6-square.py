#!/usr/bin/python3
class Square:
    """type class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Init the square class
        Args:
        param1: size is the type int attribute to make it private
        param2: position is type int attribute the position of the
        new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Private attribute to get the size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """private tribute to get the postion of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area os the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print("")
            return

        [print("")for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
