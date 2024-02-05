#!/usr/bin/python3
"""isinstance: objects !
type ints
"""


def is_kind_of_class(obj, a_class):
    """returns true if it int or objects!
    """

    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
