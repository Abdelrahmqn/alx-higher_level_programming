#!/usr/bin/python3
# from 5 continue to 6
# raise message on specific errors : area() is not implemented
"""define a class BaseGeometry
"""


class BaseGeometry:
    """raises with error messages
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
