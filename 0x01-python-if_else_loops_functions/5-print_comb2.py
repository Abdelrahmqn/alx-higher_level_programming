#!/usr/bin/python3
numbers = range(0, 100)
for i, number in enumerate(numbers):
    if number < 10:
        print("0{:d}".format(number), end="")
    else:
        print("{:d}".format(number), end="")
    if i != len(numbers) - 1:
        print(", ", end="")
