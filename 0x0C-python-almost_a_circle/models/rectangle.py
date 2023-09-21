#!/usr/bin/python3

"""this the model base containing the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """the class Rectangle inherited fronm Base class
    Why private attributes with getter/setter? Why not
    directly public attribute?

    Because we want to protect attributes of our class.
    With a setter, you are able to validate what a developer
    is trying to assign to a variable. So after,
    in your class you can “trust” these attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init constructor
        args:
        width: the width of rectangle instance attribute
        height: the height of rectangle instance attribute
        x = an other args
        y: an other args"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter value assign value to width"""
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value
        return self.__width

    @property
    def height(self):
        """getter method for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter value assign value to __height"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = value
        return self.__height

    @property
    def x(self):
        """getter method for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter value assign value to __x"""

        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = value
        return self.__x

    @property
    def y(self):
        """getter method for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter value assign value to __y"""

        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = value
        return self.__y

    def area(self):
        """public method def area(self): that returns the
        area value of the Rectangle instance."""

        return self.width * self.height

    def display(self):
        """public method def area(self): that returns the
        area value of the Rectangle instance."""
        """instance method: this  instance method that prints
        the square based on __size
        no args are given we could access to the _ssize using self
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            print(string)
        for inc in range(self.y):
            string += '\n'
        x = self.x
        for element in range(self.__height):
            for pos in range(x):
                string += ' '
            for item in range(self.__width):
                string += f"#"
            if element == self.__height - 1:
                break
            string += '\n'
        print(string)

    def __str__(self) -> str:
        """overriding the __str__ method"""
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """A public method def update(self, *args):
        that assigns an argument to each attribute:"""

        attr = ["id", "width", "height", "x", "y",]
        for i in range(len(args)):
            if i >= len(attr):
                break
            self.__setattr__(attr[i], args[i])
        for i in range(len(attr)):
            if attr[i] in kwargs.keys():
                self.__setattr__(attr[i], kwargs[attr[i]])
