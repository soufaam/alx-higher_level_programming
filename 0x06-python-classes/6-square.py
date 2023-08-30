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
    def __init__(self, size=0, position=(0, 0)):
        """
         The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
        Args:
            size (int): Description of `param1`.
            position (tuple): the position integer
        """
        if "int" not in str(type(size)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if "tuple" not in str(type(position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) and not\
                isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
    """  Attributes:
        __size:   The size of a square is crucial for a square
        __postion: the position when we start printing"""
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

    @property
    def position(self):
        """position getter method: this method get the position
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method: this method set the __postion to value
        Args:
            value (int): set the __postion to value.
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if "tuple" not in str(type(value)):
            raise TypeError("position must be a tuple\
            of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """instance method: this  instance method that prints
        the square based on __size
        no args are given we could access to the _ssize using self
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if self.__size == 0:
            print()
        for element in range(self.__size):
            x = self.__position[0]
            for pos in range(x):
                if self.__position[1] > 0:
                    break
                print(" ", end='')
            for item in range(self.__size):
                print("#", end='')
            print()

    pass
