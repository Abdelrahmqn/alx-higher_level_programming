#!/usr/bin/python3
from sys import argv
print("{} arguments:".format(len(argv) - 1))
if len(argv) > 1:
    for i, args in enumerate(argv[1:], start=1):
        print("{:d}".format(i), end="")
        print(":", args)
