#!/usr/bin/python3
"""inherits from Geometrybase class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from Geometrybase class and test the width and height
    """
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)

        self.__height = height
        self.integer_validator("height", height)
