#!/usr/bin/python3

""" This is a decription of this module .
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
BaseGeometry module contains BaseGeometry class implemetation
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """This is a class BaseGeometry summary, it's a empty
    class that defines a BaseGeometry
    there is no attributes yet
    Square that inherit from  a Rectangle
    there is no attributes yet
    """
    def __init__(self, size):
        """If the function contains notable behavior, it should be
        mentioned here.
        args:
            size of rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """If the function contains notable behavior, it should be
        mentioned here.
        args:
            size of rectangle
        """
        return super().area()
