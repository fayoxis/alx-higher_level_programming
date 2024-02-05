#!/usr/bin/python3
"""
This code defines a class called BaseGeometry, which is
based on the code in the file 5-base_geometry.py.
"""


class BaseGeometry:
    """
    This class represents a BaseGeometry.
    """

    def area(self):
        """
        This method calculates the area of the geometry.

        Raises:
            Exception: If the area is not implemented.
        """
        raise Exception("area() is not implemented")
