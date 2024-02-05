#!/usr/bin/python3
# from 5 continue to 6
# raise message on specific errors : area() is not implemented
"""defines a baseGeometry
"""


class BaseGeometry:
    """there are no area any more!
    """
    def area(self):
        raise Exception("area() is not implemented")
