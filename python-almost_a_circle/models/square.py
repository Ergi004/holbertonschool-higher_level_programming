#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization attributes
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
