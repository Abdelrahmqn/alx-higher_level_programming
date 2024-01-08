#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for matrx in matrix:
        if len(matrx) == 0:
            print()
        for i in range(len(matrx)):
            if i is len(matrx) - 1:

                print(end="\n""{:d}".format(matrix[i]) else " ")