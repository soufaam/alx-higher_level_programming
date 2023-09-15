#!/usr/bin/python3
""" This is a decription of this module .
this module contains to_json_sring function that takes myobject
as parameter
"""


def pascal_triangle(n):
    """ This is a decription of this function.
    This function reads a text file (UTF8) and prints it to stdout:
    Prototype: pascal_triangle:
    Args:
    to_json_string: jsonify a string"""

    pascalist = []
    if (n <= 0):
        return pascalist
    pascalist.append([1])
    if n > 2:
        pascalist.append([1, 1])
    elif n == 2:
        pascalist.append([1, 1])
        return pascalist
    else:
        return pascalist
    new_list = [1, 1]
    for i in range(2, n):
        old_list = new_list
        new_list = []
        for j in range(len(old_list) + 1):
            if j == 0 or j == len(old_list):
                new_list.append(1)
                continue
            else:
                new_list.append(old_list[j - 1] + old_list[j])
        pascalist.append(new_list)
    return pascalist
