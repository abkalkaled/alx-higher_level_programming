#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        new_matrix = [[n**2] for n in row]
        return new_matrix
