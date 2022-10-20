#!/usr/bin/python3

"""Module `0-rectangle.py` defines an
empty class Rectangle
"""


class Rectangle:
    """Define an empty class called
    Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize attributes
        passing the instance first"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Find area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Find parameter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
