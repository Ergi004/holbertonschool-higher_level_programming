#!/usr/bin/python3
"""
Base module
"""


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.__id = id
