#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


class Square:
    def __init__(self, size):
        """
        This is the documentation for the Square class.
        The class represents a geometric square and associated operations.
        """
        self.__size = size
