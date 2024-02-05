#!/usr/bin/python3
"""object to test
"""


def is_same_class(obj, a_class):
    """is obj an exactly an instance of a_class?
    """
    if type(obj) is a_class:
        return True
    else:
        return False
