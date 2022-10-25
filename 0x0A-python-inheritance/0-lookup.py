#!/usr/bin/python3

"""Write a function that returns
the list of available attributes
and methods of an object"""


def lookup(obj):
    """Returns a list of
    available attributes and methods

    Uses:
        dir() function"""
    return dir(obj)
