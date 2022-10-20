#!/usr/bin/python3

"""Defining class Square"""


class Square:
    """Adding unto the initialization"""

    def __init__(self, size=0):
        """Run when new instance of class
        is created.
        Args:
            size (int): The size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
