#!/usr/bin/python3
"""defines a rectangle."""


class Rectangle:
    """rectangle representation."""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width of the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns self.height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        widz = ("#" * self.__width + "\n")
        if self.__width == 0 or self.__height == 0:
            return ""
        return widz * (self.__height - 1) + "#" * self.__width

    def __repr__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        """# Rectangle has args!"""
        return f"Rectangle({self.width}, {self.__height})"
