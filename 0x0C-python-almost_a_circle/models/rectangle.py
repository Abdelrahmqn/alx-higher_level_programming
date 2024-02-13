#!/usr/bin/python3
"""define a class named Base
"""
from models.base import Base


class Rectangle(Base):
    """class that defines a rectangle with methods."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """to init constructor."""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return width."""

        return self.__width

    @width.setter
    def width(self, value):
        """make sure of the value is int."""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return height."""

        return self.__height

    @height.setter
    def height(self, value):
        """height is an int."""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x must be int."""

        return self.__x

    @x.setter
    def x(self, value):
        """x is the horizontal position."""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y must be integer."""

        return self.__y

    @y.setter
    def y(self, value):
        """y is the verticle posision of the rectangle."""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle."""

        return self.__width * self.__height

    def display(self):
        """this function displays the hash with the correct width/height."""

        display_width = "#" * self.__width
        i = 0
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + display_width)

    def __str__(self):
        """string to be stdout."""

        ids = self.id
        xs = self.x
        ys = self.y
        r = f"[Rectangle] ({ids}) {xs}/{ys} - {self.width}/{self.height}"
        return r

    def update(self, *args, **kwargs):
        """update the attributes of the class."""

        ids = self.id
        xs = self.x
        ys = self.y
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self. width = kwargs['width']
        if 'height' in kwargs:
            self.height = kwargs['height']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

        return f"[Rectangle] ({ids}) {self.width}/{self.height} - {xs}/{ys}"

    def to_dictionary(self):
        """returns the dict of square."""

        heights = self.__height
        widths = self.__width
        ids = self.id
        xs = self.x
        ys = self.y
        dic = {'x': xs, 'y': ys, 'id': ids, 'height': heights, 'width': widths}
        return dic
