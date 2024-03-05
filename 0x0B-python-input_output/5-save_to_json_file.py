#!/usr/bin/python3
"""Json to write files.
"""


import json


def save_to_json_file(my_obj, filename):
    """from json file do.
    """

    with open(filename) as myfile:
        json.myfile.write(my_obj)
