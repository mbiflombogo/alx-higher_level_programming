#!/usr/bin/python3

"""Module `101-locked_class` contains class
LockedClass that prevents the user from dynamically
creating new instance attributes"""


class LockedClass:
    """prevents dynamic attribute"""
    __slots__ = ['first_name']
