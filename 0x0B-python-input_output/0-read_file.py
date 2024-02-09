#!/usr/bin/python3
"""read file with open statement and open default as a read
"""


def read_file(filename=""):
    """function to read the file text
    """

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
