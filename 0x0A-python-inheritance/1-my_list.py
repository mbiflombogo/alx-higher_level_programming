#!/usr/bin/python3

"""Write a class MyList that inherits from list
Public instance method: def print_sorted(self):
that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list
will be of type int
You are not allowed to import any module"""


class MyList(list):
    """class MyList that inherits from list"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def print_sorted(self):
        """prints the list,
        but sorted (ascending sort)"""
        print(sorted(self))
