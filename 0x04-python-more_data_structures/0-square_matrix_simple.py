#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat_func = lambda n: n**2
    square_row = lambda row: list(map(mat_func, row))
    new_matrix = list(map(square_row, matrix))
    return new_matrix
