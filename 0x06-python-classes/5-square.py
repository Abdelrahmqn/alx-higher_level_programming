#!/usr/bin/python3
"""defines a square."""


class Square:
    """describing the class square process."""
    def __init__(self, size=0):
        """Instantiation with optional."""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            idx = 0
            while idx < self.__size:
                print("#" * self.__size)
                idx += 1
