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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != (int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.___height

    @height.setter
    def height(self, value):
        if type(value) != (int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != (int):
            raise TypeError("X must be an integer")
        if value < 0:
            raise ValueError("X must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != (int):
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("Y must be >= 0")
        self.__y = value

    def area(self):
        """
        Rectangle area
        """
        return self.width * self.height

    def display(self):
        """
        Display of the rectangle
        """
        print("\n" * self.y, end="")
        for h in range(self.height):
            print(" ", end="")
            print("#", end="")

    def update(self, *args):
        """
        Update
        """
        if args:
            a_index = 0
            for arg in args:
                if a_index == 0:
                    self.id = arg
                elif a_index == 1:
                    self.width = arg
                elif a_index == 2:
                    self.height = arg
                elif a_index == 3:
                    self.x = arg
                elif a_index == 4:
                    self.y = arg
                a_index += 1

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return {

                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """
        String imlementation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
