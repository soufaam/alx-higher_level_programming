#!/usr/bin/python3

""" This is a decription of this module .

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


class Square:
    """This is a class Square summary, it's a empty class that defines a square
    there is no attributes yet
    """
    def __init__(self, size=0):
        """
         The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
        Args:
            size (int): Description of `param1`.
        """
        if "int" not in str(type(size)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
    """  Attributes:
        __size:   The size of a square is crucial for a square   """
    pass
