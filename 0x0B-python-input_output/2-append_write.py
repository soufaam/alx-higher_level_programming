#!/usr/bin/python3

""" This is a decription of this module ."""


def append_write(filename="", text=""):
    """ This is a decription of this function.
    This function reads a text file (UTF8) and prints it to stdout:
    Prototype: def read_file(filename=""):
    Args:
    filname: name of file"""
    with open(filename, "a+") as f:
        lenght = f.write(text)
    return lenght
