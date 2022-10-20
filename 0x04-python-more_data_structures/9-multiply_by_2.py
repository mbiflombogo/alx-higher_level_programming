#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {ky: a_dictionary[ky]*2 for ky in list(a_dictionary)}
