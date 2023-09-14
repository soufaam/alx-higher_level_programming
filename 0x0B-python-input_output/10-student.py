#!/usr/bin/python3

""" This is a decription of this module .

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


class Student:
    """This is a class Square summary, it's a empty class that defines a square
    there is no attributes yet
    """

    def __init__(self, first_name, last_name, age):
        """
         The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
        Args:
            param1 (str): Description of `param1`.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """The to_json method may be documented in either the class level"""
        data = {}
        if isinstance(attrs, list):
            for item in attrs:
                if isinstance(item, str):
                    if item == "first_name":
                        if item not in data.keys():
                            data[item] = self.first_name
                    elif item == "last_name":
                        if item not in data.keys():
                            data[item] = self.last_name
                    elif item == "age":
                        if item not in data.keys():
                            data[item] = self.age
                else:
                    return self.__dict__
            if data != {}:
                return data
            else:
                return self.__dict__
        else:
            return self.__dict__
