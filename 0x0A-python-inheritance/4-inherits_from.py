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


def inherits_from(obj, a_class):
    """inherits_from function:
    args:
        obj : is a object.
        a_class: class type
        If the function contains notable behavior, it should be
    mentioned here.
    """
    return isinstance(obj, a_class)
a = [1, 2, 3]
print(inherits_from(a, list))