#!/usr/bin/python3

""" This is a decription of this module .

This module contains a function called add_integer
that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over
multiple lines. Sections are created
with a section header and a colon followed
by a block of indented text.
"""


def matrix_divided(matrix, div):
    """a function that adds 2 integers.
    Prototype: def matrix_divided(matrix, div):
    args:
    matrix:  must be a list of lists of integers or floats
    div: iv must be a number (integer or float),
    matrix must be a matrix (list of lists)\
    of integers/floats
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b"""

    new_matrix = []
    size = 0
    i = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    for row in matrix:
        if isinstance(row, list):
            if i >= 1 and len(row) != size:
                raise TypeError("Each row of the matrix must\
 have the same size")
            size = len(row)
            newrow = []
            for item in row:
                if not isinstance(item, int) and not isinstance(item, float):
                    raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                newrow.append(round(item / div, 2))
        else:
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        i += 1
        new_matrix.append(newrow)
    return new_matrix
