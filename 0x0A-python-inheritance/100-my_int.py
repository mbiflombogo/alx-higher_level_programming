#!/usr/bin/python3

"""Write a class MyInt that inherits int"""


class MyInt(int):
    """MyInt extends `int`"""
    def __new__(cls, *args, **kwargs):
        """Initialize"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Equals: =="""
        return int(self) != other

    def __ne__(self, other):
        """Not equals: !="""
        return int(self) == other
