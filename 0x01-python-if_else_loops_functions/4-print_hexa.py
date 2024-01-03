#!/usr/bin/python3
number = range(1, 10)
chars = range(ord('a'), ord('f') + 1)
nums = range(10, 18)
for i in number:
    for j in range(1, 10):
        print(f"{j:d} = 0x{i:d}")
        print
