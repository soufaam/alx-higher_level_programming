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
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
