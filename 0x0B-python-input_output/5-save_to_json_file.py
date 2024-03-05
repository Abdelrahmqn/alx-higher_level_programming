#!/usr/bin/python3
"""Json to write files.
"""


import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes an Object
      to a text file, using a JSON representation:
    """

    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
