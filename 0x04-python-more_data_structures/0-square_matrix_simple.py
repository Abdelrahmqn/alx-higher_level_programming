#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [list(map(lambda number: number ** 2, i)) for i in matrix]
    return new
