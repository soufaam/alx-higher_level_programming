#!/usr/bin/python3

""" This is a decription of this module .
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
BaseGeometry module contains BaseGeometry class implemetation
"""


def add_attribute(obj, attr, value):
    """ function check if it's possible to add attribute"""

    try:
        obj.__setattr__(attr, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
