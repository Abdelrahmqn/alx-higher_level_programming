#!/usr/bin/python3
"""inherits from Geometrybase class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from Geometry and do area str return
    """

    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)

        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return str(f"[Rectangle] {self.__width}/{self.__height}")
