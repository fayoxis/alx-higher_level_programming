#!/usr/bin/python3
"""
This script defines a class called MyInt that inherits from the int class.
MyInt is a rebellious class that flips the behavior of the == and != operators.
"""


class MyInt(int):
    """
    The MyInt class represents an integer with inverted equality operators.

    Args:
        int (int): The value of the integer.
    """
    def __init__(self, value):
        """
        Initializes a new instance of the MyInt class.

        Args:
            value (int): The integer value.
        """
        self.__value = value

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other (int): The other integer to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.__value != other

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other (int): The other integer to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.__value == other
