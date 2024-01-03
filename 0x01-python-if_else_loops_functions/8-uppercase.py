#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        res += chr(ord(char) - 32)
    else:
        res += char
        print("{}".format(res))
