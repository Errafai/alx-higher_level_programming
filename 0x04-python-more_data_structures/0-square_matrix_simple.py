#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in matrix:
        row = [ j ** 2 for j in i]
        m.append(row)
    return m
