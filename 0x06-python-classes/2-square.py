#!/usr/bin/python3
"""defines a square."""


class Square:
    def __init__(self, size=0):
        """size must be bigger than or equall zero."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
