#!/usr/bin/python3
""" This is a decription of this module .
this module contains append_after function that takes myobject
as parameter
"""


def append_after(filename="", search_string="", new_string=""):
    """ This is a decription of this function.
    This function reads a text file (UTF8) and prints it to stdout:
    Prototype: append_after:
    Args:
    append_after: jsonify a string"""

    lines = []
    listindex = []
    new_lines = []
    with open(filename, "r") as rfile:
        lines = rfile.readlines()
        for index in range(len(lines)):
            if lines[index].find(search_string) != -1:
                listindex.append(index)
    for iter in range(len(lines)):
        new_lines.append(lines[iter])
        for index in listindex:
            if index == iter:
                new_lines.append(new_string)
    with open(filename, "w") as wfile:
        wfile.writelines(new_lines)
