#!/usr/bin/python3
def read_file(filename=""):
    filename = "my_file_0.txt"
    with open(filename, encoding="utf-8") as myfile:
        myfile.read()
