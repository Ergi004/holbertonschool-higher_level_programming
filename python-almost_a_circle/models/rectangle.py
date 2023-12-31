#!/usr/bin/python3
"""
Rectanle module
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initalization the attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Rectangle area
        """
        return self.height * self.width

    def display(self):
        """
        Display of the rectangle
        """
        if self.y != 0:
            print("\n" * (self.y - 1))
        for _ in range(self.height):
            if self.x != 0:
                print(' ' * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''
        Function to update instance variables
        '''
        attribute_names = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            if i < len(attribute_names):
                setattr(self, attribute_names[i], value)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Function to return dictionary
        representation of a Rectangle
        '''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
