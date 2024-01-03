#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a + 1, 10):
        print(f"{a}{b:0d}", end="")
        if a != 8 or b != 9:
            print(", ", end="")
