#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for n in matrix:
        new_r = []
        for v in n:
            new_r.append(v ** 2)
        new_list.append(new_r)
    return new_list

