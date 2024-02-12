#!/usr/bin/python3
"""importing the methods
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """defines a square and inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """notice here we used size.__init__ twice ,
        size takes two places height/width.
        """

        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """return the correct order."""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

    @property
    def size(self):
        """return the correct size."""

        return self.__size

    @size.setter
    def size(self, value):
        """size or size of rectangles. anything else.
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the value by using updating the update methods."""

        xs = self.x
        ys = self.y
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'size' in kwargs:
            self.__size = kwargs['size']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
        return f"[Square] ({self.id}) {self.size}/{self.size} - {xs}/{ys}"
