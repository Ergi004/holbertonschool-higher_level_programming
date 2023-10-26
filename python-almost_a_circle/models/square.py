#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


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
        return self.width

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

    def update(self, *args, **kwargs):
        """
        Function to update attributes
        """
        name_list = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            setattr(self, name_list[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        '''
        Function to return dictionary
        representation of a Rectangle
        '''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
