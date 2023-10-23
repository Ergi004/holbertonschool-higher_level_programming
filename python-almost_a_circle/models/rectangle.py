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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
