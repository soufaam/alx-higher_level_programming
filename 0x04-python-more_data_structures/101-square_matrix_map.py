#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(map(lambda x, y: x * y, matrix, matrix), matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)