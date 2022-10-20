#!/usr/bin/python3

"""
Module 4-print_square contains
one function print_square()
that prints a square using `#`
"""


def print_square(size):
    """Print square of size 'size'

    Args:
        size (int): length of square

    Raises:
        TypeError: if size !int, and if float & < 0
        ValueError: if size < 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
