#!/usr/bin/python3
"""Defines a class Rectangle"""

class Rectangle:
    """
    The `Rectangle` class represents a rectangle object with a given width and height. 
    - `number_of_instances`: A class attribute that keeps track of the number of `Rectangle` instances created.
    - `print_symbol`: A class attribute that represents the symbol used to print the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a `Rectangle` object with the specified width and height. 
        Args:
        - `width`: The width of the rectangle (default: 0).
        - `height`: The height of the rectangle (default: 0).
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        A property that returns the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A setter method for the width attribute. It validates that the width is a positive integer.
        
        Args:
        - `value`: The value to set as the width of the rectangle.
        
        Raises:
        - `TypeError`: If the value is not an integer.
        - `ValueError`: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        A property that returns the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A setter method for the height attribute. It validates that the height is a positive integer.
        
        Args:
        - `value`: The value to set as the height of the rectangle.
        
        Raises:
        - `TypeError`: If the value is not an integer.
        - `ValueError`: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        
        Returns:
        - The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        
        Returns:
        - The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle, using the `print_symbol` 
        
        Returns:
        - A string representation of the rectangle.
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to recreate the object.
        
        Returns:
        - A string representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when the rectangle object is deleted and decrements
        the `number_of_instances` attribute by 1.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two `Rectangle` objects and returns the one with a greater or equal area.
        
        Args:
        - `rect_1`: The first rectangle to compare.
        - `rect_2`: The second rectangle to compare.
        
        Raises:
        - `TypeError`: If either `rect_1` or `rect_2` is not an instance of `Rectangle`.
        
        Returns:
        - The `Rectangle` object with a greater or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2
