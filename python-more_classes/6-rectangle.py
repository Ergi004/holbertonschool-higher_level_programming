#!/usr/bin/python3

'''
    Simple module for creating a
    Rectnagle class with instance methods
    and class methods
'''


class Rectangle:
    '''
        Rectangle class with two attributes

    '''
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''
            Init function for Rectangle class

        '''
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
            Width attribute getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Width attribute setter
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
            Height attribute getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Height attribute setter
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        Area of rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
        Perimeter of rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        '''
        Pringing the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return (f"")

        print_rec = []
        for i in range(self.__height):
            for c in range(self.__width):
                print_rec.append("#")
            if i < self.__height - 1:
                print_rec.append("\n")

        return "".join(print_rec)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
