#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Class that inherits from list.

    Args:
        list (list): The list to be sorted in ascending order.
    """

    def print_sorted(self):
        """Prints the elements of the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
