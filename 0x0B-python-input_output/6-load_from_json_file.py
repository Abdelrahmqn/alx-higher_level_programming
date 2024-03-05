#!/usr/bin/python
"""the module documentation json
"""


import json


def load_from_json_file(filename):
    """creates a new object from the json file
    """

    with open(filename, 'r') as mfile:
        return json.load(filename)
