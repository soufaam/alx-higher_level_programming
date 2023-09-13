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


class MyList(list):
    """This is a class MyList summary, it's a empty
    class that defines a MyList"""
    def print_sorted(self):
        """print_sorted function:
        value (int): set the _size to value.
    If the print_sorted contains notable behavior,
    it should be
    mentioned here.
    """
        self.sort()
        print(self)
