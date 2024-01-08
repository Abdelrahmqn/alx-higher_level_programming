#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for r in range(len(matrix)):
        for e in range(len(matrix[r])):
            print("{} ".format(matrix[r][e]), end="")
        print()