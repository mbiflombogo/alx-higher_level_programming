#!/usr/bin/python3

"""Say my name
A function that prints my name"""


def say_my_name(first_name, last_name=""):
    """Print first name and last name

    Args:
        first_name (str): name 1
        last_name (str): name 2, default--> empty string
    Raises:
        TypeError: if name 1 or name 2 not string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
