#!/usr/bin/python3
"""defines a square."""


class Square:
    """describing the class square process."""
    def __init__(self, size=0):
        """size must be bigger than or equall zero."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
