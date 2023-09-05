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
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
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

    def area(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns the square of size
        """
        return self.__width * self.__height

    def perimeter(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns the square of size
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self) -> str:
        """instance method __str__: this  instance method that prints
        the square based on __height and __width it's like my_print()
        method it returns a string
        no args are given we could access to the _ssize using self
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for element in range(self.__height):
            for item in range(self.__width):
                string += f"{self.print_symbol}"
            if element == self.__height - 1:
                break
            string += '\n'
        return string

    def __repr__(self) -> str:
        """instance method __repr__: this  instance method that prints
        the square based on __height and __width it's like my_print()
        method it returns a string
        no args are given we could access to the _ssize using self
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        x = self.__width
        y = self.__height
        return "Rectangle({}, {})".format(x, y)

    def __del__(self):
        """instance method __del__: this  instance method that prints
        the square based on __height and __width it's like my_print()"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """instance method __repr__: this  instance method that prints
        the square based on __height and __width it's like my_print()
        method it returns a string
        no args are given we could access to the _ssize using self
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """instance method __repr__: this  instance method that prints
        the square based on __height and __width it's like my_print()
        method it returns a string
        no args are given we could access to the _ssize using self
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")
        return cls(size, size)
