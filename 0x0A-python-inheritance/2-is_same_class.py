#!/usr/bin/python3

""" This is a decription of this module .

This module contains a function called is_same_class
that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over multiple
lines. Sections are created
with a section header and a colon followed by a
block of indented text.
"""


def is_same_class(obj, a_class):
    """is_same_class function:
    args:
        obj : is a object.
        a_class: class type
        If the function contains notable behavior, it should be
    mentioned here.
    """
    if str(a_class) in str(type(obj)):
        return True
    else:
        return False
