#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""

class Rectangle:
    """
    Represents a rectangle with a given width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle. Defaults set to 0.
            height (int, optional): The height of the rectangle. Defaults set to 0.
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns the string representating rectangle using '#' characters.

        Returns:
            str: The rectangle is a string.
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        # Remove the last newline character
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """
        Returns the string representating rectangle.

        Returns:
            str: The rectangle representation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Deletes an instance of the Rectangle class.
        """
        print("Rectangle instance has been deleted.")

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        elif value < 0:
            raise ValueError("Width must be >= 0.")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        elif value < 0:
            raise ValueError("Height must be >= 0.")
        else:
            self.__height = value

    def area(self):
        """
        Calculates  area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
