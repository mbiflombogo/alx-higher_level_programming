#!/usr/bin/python3
def uppercase(str):
    s = ""
    for c in str:
        if ord(c) == 32:
            s += c
        elif 64 < ord(c) < 91:
            s += c
        elif 96 < ord(c) < 123:
            s += chr(ord(c) - 32)
        else:
            s += c
    print("{}".format(s))
