#!/usr/bin/python3
"""return the names in the current scope
otherwise default
 """


def lookup(obj):
    """lookup for objects"""

    return dir(obj)
