#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        _format = ' '.join(map(str, row))
        print("{}".format(_format))