#!/usr/bin/python3

""" This is a decription of this module .

This module contains a function called add_integer
that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over multiple
lines. Sections are created
with a section header and a colon followed by a
block of indented text.
"""


def add_integer(a, b=98):
    """a function that adds 2 integers.
    Prototype: def add_integer(a, b=98):
    args:
    a: is integer or is float
    b: is integer or flaot
    a and b must be integers or floats, otherwise raise
    a TypeError exception with the message a must be an
    integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b"""

    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        return int(a) + int(b)
    elif isinstance(a, int) and isinstance(b, float):
        return int(a) + int(b)
    elif isinstance(b, int) and isinstance(a, float):
        return int(a) + int(b)
    elif not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
