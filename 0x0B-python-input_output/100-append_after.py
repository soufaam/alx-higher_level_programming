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

    with open(filename, "r") as rfile:
        lines = rfile.readlines()
        for index in range(len(lines)):
            if lines[index].find(search_string) != -1:
                lines.insert(index + 1, new_string)
        print(lines)
    with open(filename, "w") as wfile:
        wfile.writelines(lines)
