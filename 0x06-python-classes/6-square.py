#!/usr/bin/python3
"""defines a square."""


class Square:
    """describing the class square process."""
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """the position of the square."""
        if value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area."""
        return self.__size ** 2

    def my_print(self):
        """print square with the character #."""
        if self.__size == 0:
            print()
        elif self.__position[1] > 0:
            print()
        else:
            idx = 0
            while idx < self.__size:
                print("#" * self.__size)
                idx += 1
