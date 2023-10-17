#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle
    """

    def __init__(self, width, height):
        """
        Subclass of Base Geometry
        """
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        to_str = "[Rectangle] "
        to_str += str(self.__width) + '/' + str(self.__height)
        return to_str
