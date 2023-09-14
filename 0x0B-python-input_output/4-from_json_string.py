#!/usr/bin/python3
""" This is a decription of this module .
this module contains to_json_sring function that takes myobject
as parameter
"""
from json import loads


def from_json_string(my_str):
    """ This is a decription of this function.
    This function reads a text file (UTF8) and prints it to stdout:
    Prototype: def read_file(filename=""):
    Args:
    to_json_string: jsonify a string"""

    return loads(my_str)
