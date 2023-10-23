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
        self.__width = value
        if value is not (int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Hidht must be > 0")

    @property
    def height(self):
        return self.___height

    @height.setter
    def height(self, value):
        self.__height = value
        if value is not (int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height mist be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if value is not (int):
            raise TypeError("X must be an integer")
        if value <= 0:
            raise ValueError("X mist be > 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if value is not (int):
            raise TypeError("Y must be an integer")
        if value <= 0:
            raise ValueError("Y mist be > 0")

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print(" ", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} {self.width}/{self.height}"

    def update(self, *args):
        for index, value in enumerate(args):
            if index == 0:
                self.id = args[index]
            if index == 1:
                self.width = args[index]
            if index == 2:
                self.height = args[index]
            if index == 3:
                self.x = args[index]
            if index == 4:
                self.y = args[index]
