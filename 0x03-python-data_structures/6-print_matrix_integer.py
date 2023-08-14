#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for idx in range(len(item)):
            if idx == len(item) - 1:
                print("{:d}".format(item[idx]), end="")
            else:
                print("{:d}".format(item[idx]), end=" ")
        print()
