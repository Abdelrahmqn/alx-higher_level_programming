#!/usr/bin/python
"""the module documentation json
"""


import json


def load_from_json_file(filename):
    with open(filename, 'r') as mfile:
        return json.load(filename)
