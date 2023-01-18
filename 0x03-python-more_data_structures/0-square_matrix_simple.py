#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        new = []
        for rows in matrix:
            new.append(list(map(lambda x: x**2, rows)))
        return (new)
    return None