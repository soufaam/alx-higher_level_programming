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
    def area(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns the square of size
        """
        return self.__size ** 2

    @property
    def size(self):
        """size() method: this is getter method, we can just read only."""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method: this method set the __size to value
        Args:
            value (int): set the _size to value.
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if "int" not in str(type(value)):
            raise TypeError("size must be an integer")
        self.__size = value
    pass
