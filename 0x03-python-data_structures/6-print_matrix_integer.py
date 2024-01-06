#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for amod in matrix:
        for element in amod:
            print("{}".format(element), end=" ")
        print()
