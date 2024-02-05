#!/usr/bin/python3
"""
Write a function that prints a text
with 2 new lines after each of these characters:=> '.', '?' and ':' .
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == ".":
            print()
            print()
        elif i == "?":
            print()
            print()
        elif i == ":":
            print()
            print()
        else:
            print(i.strip(), end="")
