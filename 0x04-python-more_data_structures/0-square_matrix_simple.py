#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    for ls in matrix:
        new_m.append([el**2 for el in ls])
    return new_m
