#!/usr/bin/python3
"""the module documentation json
"""

import json


def load_from_json_file(filename):
    """creates a new object from the json file
    """

    with open(filename, 'r', encoding="UTF-8") as mfile:
        return json.load(mfile)
