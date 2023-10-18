#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'python3 -c 'print(__import__("my_module").__doc__)'
"""


def read_file(filename=""):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    with open(filename, encoding="utf-8") as f:
        read_f = f.read()
        print(read_f)
