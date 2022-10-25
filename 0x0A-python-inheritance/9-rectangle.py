#!/usr/bin/python3

"""Write a class Rectangle
that inherits BaseGeometry"""


class BaseGeometry:
    """defines public instance method
    called area()"""
    def area(self):
        """Finds area else raises
        exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if of type int and if > than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle extends BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
