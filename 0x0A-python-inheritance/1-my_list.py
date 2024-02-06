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
        list_ = self[:]
        list_.sort()
        print(list_)
