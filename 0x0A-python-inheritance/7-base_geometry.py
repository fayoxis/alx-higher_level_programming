#!/usr/bin/python3
"""Defines the BaseGeometry class based on the 6-base_geometry.py file."""


class BaseGeometry:
    """A class representing basic geometry operations."""
    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: If the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        while value <= 0:
            raise ValueError(f"{name} must be greater than 0")
