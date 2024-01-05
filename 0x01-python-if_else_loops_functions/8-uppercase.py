#!/usr/bin/python3


def lower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    for char in str:
        print(chr(ord(char) - 32) if lower(char) else char, end="")
    print("")
