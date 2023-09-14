#!/usr/bin/python3
""" This is a decription of this module .
this module contains save_to_json_file function that takes myobject
as parameter
"""
from json import load


def load_from_json_file(filename):
    """ This is a decription of this function.
    This function reads a text file (UTF8) and prints it to stdout:
    Prototype: def read_file(filename=""):
    Args:
    save_to_json_file: jsonify a string"""

    with open(filename, "r") as f:
        lt = load(f)
    return lt
