#!/usr/bin/python3
'''
    This script defines a Square class.
'''

class Square:
    '''
    A Square class that represents a square shape.
    '''

    def __init__(self, side=0):
        '''
        Initializes a new instance of the Square class.

        Args:
            side (int): The side length of the square.
        '''
        self.side = side

    @property
    def side(self):
        '''
        Retrieves the side length of the square.

        Returns:
            The side length of the square.
        '''
        return self.__side

    @side.setter
    def side(self, value):
        '''
        Sets the side length of the square.

        Args:
            value (int): The side length of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("side length must be an integer")
        if value < 0:
            raise ValueError("side length must be >= 0")
        self.__side = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            The area of the square.
        """
        return self.__side * self.__side

    def perimeter(self):
        """
        Computes the perimeter of the square.

        Returns:
            The perimeter of the square.
        """
        return self.__side * 4

    def __str__(self):
        '''
        Returns a string representation of the Square object.

        Returns:
            A string representation of the Square object.
        '''
        square_string = ""
        if self.__side == 0:
            return square_string
        else:
            for i in range(0, self.__side):
                for j in range(0, self.__side):
                    square_string += "*"
                square_string += "\n"
            return square_string[:-1]

    def __repr__(self):
        return "Square({})".format(self.__side)

    def __del__(self):
        print("Bye square...", flush=True)
