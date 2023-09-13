#!/usr/bin/python3

""" This is a decription of this module .
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
BaseGeometry module contains BaseGeometry class implemetation
"""


class BaseGeometry:
    """This is a class BaseGeometry summary, it's a empty
    class that defines a BaseGeometry
    there is no attributes yet
    """
    def area(self):
        """If the function contains notable behavior, it should be
    mentioned here.
    """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """If the function contains notable behavior, it should be
    mentioned here.
    """
        if "int" not in str(type(value)):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """This is a class BaseGeometry summary, it's a empty
    class that defines a BaseGeometry
    there is no attributes yet
    """
    def __init__(self, width, height):
        """If the function contains notable behavior, it should be
        mentioned here.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """If the function contains notable behavior, it should be
        mentioned here.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """If the function contains notable behavior, it should be
        mentioned here.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """This is a class BaseGeometry summary, it's a empty
    class that defines a BaseGeometry
    there is no attributes yet
    """
    def __init__(self, size):
        """If the function contains notable behavior, it should be
        mentioned here.
        """
        super().__init__(size, size)
