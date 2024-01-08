#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        _format = ' '.join(map(str, row))
        print("{}".format(_format))
