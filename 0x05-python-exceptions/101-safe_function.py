#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as inst:
        print("Exception:", inst, file=sys.stderr)
        return None
