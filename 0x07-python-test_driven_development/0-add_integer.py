#!/usr/bin/python3
"""
    a: int
    b: int
        a + b is int.
"""


def add_integer(a, b=98):
    """
    function that adds two integers.
    funciton must do :
    a and b must be first casted to integers if they are float.
"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
