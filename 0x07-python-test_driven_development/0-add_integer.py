#!/usr/bin/python3

"""
Module contains one function: add_integer()
that adds two no. floats and ints and returns
the outcome
"""


def add_integer(a, b=98):
    """Returns addition of two no. of type int
    or float
    Args:
        a (int): num_first
        b (int, optional): num_two Default--> 98
    Raises:
        TypeError: a and b must be an integer
    Returns:
        int: addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
