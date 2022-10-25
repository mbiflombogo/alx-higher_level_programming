#!/usr/bin/python3

"""Write a class BaseGeometry
Public instance method: def area(self)"""


class BaseGeometry:
    """defines public instance method
    called area()"""
    def area(self):
        """Finds area else raises
        exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if of type int and if > than 0"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
