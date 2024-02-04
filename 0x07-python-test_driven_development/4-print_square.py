#!/usr/bin/python3
"""square size."""


def print_square(size):
    """print the size mul with the character "#" ."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, (float)) < 0:
        raise TypeError("size must be an integer")
    index = 0
    for index in range(size):
        print(size * "#")
        index += 1
