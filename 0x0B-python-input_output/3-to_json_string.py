#!/usr/bin/python3
""" This is a decription of this module .
this module contains to_json_sring function that takes myobject
as parameter
"""
from json import dumps


def to_json_string(my_obj):
    """ This is a decription of this function.
    This function reads a text file (UTF8) and prints it to stdout:
    Prototype: def read_file(filename=""):
    Args:
    to_json_string: jsonify a string"""

    return dumps(my_obj)
