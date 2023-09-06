#!/usr/bin/python3

""" This is a decription of this module .

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


class LockedClass:
    """This is a class Square summary, it's a empty
    class that defines a square
    there is no attributes yet
    """
    __slots__ = ['first_name']

    def __init__(self, fn=None):
        """
        The __init__ method may be documented in
        either the class level
        docstring, or as a docstring on the __init__
        method itself.
        Args:
            param1 (str): Description of `param1`.
        """
        self.first_name = fn
