#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_list = []
    for j in range(len(matrix)):
        for item in matrix[j]:
            new_list.append(item ** 2)
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
