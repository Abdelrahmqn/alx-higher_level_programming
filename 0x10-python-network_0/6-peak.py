#!/usr/bin/python3
"""file documentation python."""


def find_peak(list_of_integers):
    """function documention finding the peak number
    """
    if not list_of_integers:
        return None
    list_of_integers = sorted(list_of_integers)
    return list_of_integers[-1]
