#!/usr/bin/python3

"""
Module 5-text_indentation contains
function text_indentation() that
prints a text with 2 new lines after
each of these characters: . ? and :
"""


def text_indentation(text):
    """Prints text with 2 new lines
    Args:
        text (str): txt to be printed
    Raises:
        TypeError: if text !str
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    hld = 0
    for char in text:
        if hld == 0:
            if char == ' ':
                continue
            else:
                hld = 1
        if hld == 1:
            if char in ['.', '?', ':']:
                print(char)
                print()
                hld = 0
            else:
                print(char, end="")
