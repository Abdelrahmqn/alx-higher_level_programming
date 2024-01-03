#!/usr/bin/python3
chars = range(ord('a'), ord('z') + 1)
for i in chars:
    if chr(i) != 'e' and chr(i) != 'q':
        print("{}".format(chr(i)), end="")
