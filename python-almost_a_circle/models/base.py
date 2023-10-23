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
        self.__id = id
        if id is not None:
            self.id = id
        self.id = nb_objects
