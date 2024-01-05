#!/usr/bin/python3


def lower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    res = ""
    for char in str:
        res += chr(ord(char) - 32) if lower(char) else char
        print("{}".format(res))
