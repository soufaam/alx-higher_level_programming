#!/usr/bin/python3

""" This is a decription of this module .

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


class Rectangle:
    """This is a class Square summary, it's a empty class that defines a square
    there is no attributes yet
    """
    def __init__(self, width=0, height=0):
        """
         The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
        Args:
            param1 (str): Description of `param1`.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    """  Attributes:
        __width: width must be an integer,
        __height: height must be an integer"""

    @property
    def height(self):
        """height() method: this is getter method, we can just read only
        and retreive the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method: this method set the height to value
        Args:
            value (int): set the __heihgt to value.
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width() method: this is getter method, we can just read only,
        and retreive the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method: this method set the width to value
        Args:
            value (int): set the __width to value.
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
