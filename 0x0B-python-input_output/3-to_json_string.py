#!/usr/bin/python3
import json


""" This is a decription of this module ."""


def to_json_string(my_obj):
    """ This is a decription of this function.
    This function reads a text file (UTF8) and prints it to stdout:
    Prototype: def read_file(filename=""):
    Args:
    filname: name of file"""

    return json.dumps(my_obj)
