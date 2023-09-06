#!/usr/bin/python3

""" This is a decription of this module .

This module contains a function called say_my_name
that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over
multiple lines. Sections are created
with a section header and a colon followed
by a block of indented text.
"""


def print_square(size):
    """a function that adds 2 integers.
    Prototype: def print_square(size):
    args:
    first_name:  must be strings
    last_name:  must be strings
    A function that prints My name is <first name> <last name>"""

    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for elt in range(size):
        for item in range(size):
            print("#", end='')
        print()
