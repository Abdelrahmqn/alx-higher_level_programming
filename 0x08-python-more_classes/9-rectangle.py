#!/usr/bin/python3
# join() method takes all items in an iterable and joins them into one string
# string must be specified as the separator.
"""defines a rectangle."""


class Rectangle:
    """rectangle representation."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
        ret = (str(self.print_symbol) * self.__width + "\n")
        ret1 = ret * (self.__height - 1)
        if self.__width == 0 or self.__height == 0:
            return ""
        return ret1 + str(self.print_symbol) * self.__width

    def __repr__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        """# Rectangle has args!"""
        return f"Rectangle({self.width}, {self.__height})"

    def __del__(self):
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        area1, area2 = rect_1.area(), rect_2.area()
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
