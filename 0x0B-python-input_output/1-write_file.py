#!/usr/bin/python3
"""defines a function that writes something
"""


def write_file(filename="", text=""):
    """function that writes contents to file
    """

    with open(filename, 'w', encoding="utf-8") as myfile:
        return myfile.write(text)
