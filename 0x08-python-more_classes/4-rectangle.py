#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self._height = height
        self._width = width

    @property
    def width(self):
        """Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @property
    def height(self):
        """Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        elif value < 0:
            raise ValueError("Width must be a non-negative integer.")
        else:
            self._width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        elif value < 0:
            raise ValueError("Height must be a non-negative integer.")
        else:
            self._height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._height * self._width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self._height == 0 or self._width == 0:
            return 0
        else:
            return 2 * (self._height + self._width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        rectangle = []

        if self._width == 0 or self._height == 0:
            return ""

        for i in range(self._height):
            for j in range(self._width):
                rectangle.append("#")
            rectangle.append("\n")

        # Remove the last newline character
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self._width, self._height)
