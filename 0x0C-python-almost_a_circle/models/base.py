#!/usr/bin/python3

"""this the model base containing the class Base"""


class Base:
    """the class base
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """init constructor
        args: id public instance attribute"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
