#!/usr/bin/python3
def print_last_digit(number):
    ld = int(repr(number)[-1])
    print("{}".format(ld), end="")
    return ld
