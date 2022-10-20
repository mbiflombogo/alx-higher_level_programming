#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    for ky in list(a_dictionary):
        if a_dictionary[ky] == value:
            del a_dictionary[ky]
    return a_dictionary
