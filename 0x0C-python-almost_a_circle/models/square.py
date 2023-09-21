#!/usr/bin/python3

"""this the model base containing the class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square inherited fronm Base class
    Why private attributes with getter/setter? Why not
    directly public attribute?

    Because we want to protect attributes of our class.
    With a setter, you are able to validate what a developer
    is trying to assign to a variable. So after,
    in your class you can “trust” these attributes."""

    def __init__(self, size, x=0, y=0, id=None):
        """init constructor
        args:
        width: the width of Square instance attribute
        height: the height of rectangle instance attribute
        x = an other args
        y: an other args"""

        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """overriding the __str__ method"""
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter mthod for the size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """A public method def update(self, *args):
        that assigns an argument to each attribute:"""

        attr = ["id", "size", "x", "y",]
        for i in range(len(args)):
            if i >= len(attr):
                break
            if attr[i] == "size":
                self.__setattr__("width", args[i])
                self.__setattr__("height", args[i])
                continue
            self.__setattr__(attr[i], args[i])
        for i in range(len(attr)):
            if attr[i] in kwargs.keys():
                if attr[i] == "size":
                    self.__setattr__("width", kwargs[attr[i]])
                    self.__setattr__("height", kwargs[attr[i]])
                    continue
                self.__setattr__(attr[i], kwargs[attr[i]])
