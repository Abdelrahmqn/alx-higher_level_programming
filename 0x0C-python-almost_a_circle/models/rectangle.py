#!/usr/bin/python3
"""define a class named Base
"""


class Base:
    """The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the constructor."""

        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects


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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """x is the horizontal position."""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """y is the verticle posision of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle."""

        return self.__width * self.__height

    def display(self):
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
        r = f"[Rectangle] ({ids}) <{xs}>/<{ys}> - {self.width}/{self.height}"
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
