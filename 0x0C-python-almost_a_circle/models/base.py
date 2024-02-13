#!/usr/bin/python3
"""define a class named Base
"""
import json


class Base:
    """The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """new class with const init the-purps to know the id."""

        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """return the object representation of python."""

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """json_string is a string representing a list of the dicts"""

        if json_string is None:
            return []
        else:
            return json.loads(json_string)
