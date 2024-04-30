#!/usr/bin/python3
"""this Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """ this function that finds a peak in a list of unsorted integers.
    """
    list_ = list_of_integers
    while list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
