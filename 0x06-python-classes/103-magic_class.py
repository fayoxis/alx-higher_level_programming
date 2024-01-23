#!/usr/bin/python3
"""Define a Circle class with radius and diameter attributes."""

import math


class Circle:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a Circle instance.

        Args:
            radius (float or int): The radius of the Circle.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the Circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the Circle."""
        return 2 * math.pi * self.__radius
