#!/usr/bin/python3

""" This is a decription of this module .

This module contains a function called say_my_name that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


def say_my_name(first_name, last_name=""):
    """a function that adds 2 integers.
    Prototype: def say_my_name(first_name, last_name=""):
    args:
    first_name:  must be strings
    last_name:  must be strings
    A function that prints My name is <first name> <last name>"""

    new_matrix = []
    size = 0
    i = 0
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

say_my_name()