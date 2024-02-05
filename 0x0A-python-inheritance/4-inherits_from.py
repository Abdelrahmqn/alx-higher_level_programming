#!/usr/bin/python3
"""(directly or indirectly)
return the true output
True inherited from class int
True inherited from class object"""


def inherits_from(obj, a_class):
    """inderectly or directly
    """
    if type(obj) != a_class:
        return True
    else:
        return False
