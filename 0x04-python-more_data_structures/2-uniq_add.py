#!/usr/bin/python3
def uniq_add(my_list=[]):
    ls_set = set(my_list)
    total = 0
    for i in ls_set:
        total += i
    return total
