#!/usr/bin/python3
"""defines a class named "square"
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """area and string return function is implemented
    correctly with no mistakes 99.99999998%"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
