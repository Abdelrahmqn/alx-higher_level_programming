#!/usr/bin/python3
"""append contents to the file
"""


def append_write(filename="", text=""):
    """append contents
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
