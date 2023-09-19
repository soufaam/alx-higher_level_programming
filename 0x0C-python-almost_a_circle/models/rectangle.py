#!/usr/bin/python3

"""this the model base containing the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """the class Rectangle inherited fronm Base class
    Why private attributes with getter/setter? Why not directly public attribute?

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
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if width <= 0:
            raise ValueError("width must be > 0")
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