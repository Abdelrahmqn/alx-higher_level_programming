#!/usr/bin/python3
"""try to add make function (class) that adds automaticly attributes!
"""


class attributes_to_add():
    """class to define the function new attributes
    """
    def add(self, name):
        for num, value in name.items():
            if hasattr(self, num):
                raise TypeError("can't add new attribute")
            setattr(self, num, value)
