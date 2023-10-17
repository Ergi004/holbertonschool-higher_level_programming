#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:
    """
    Geometry class
    """
    def area(self):
        raise Exception("area() is not implemented")
