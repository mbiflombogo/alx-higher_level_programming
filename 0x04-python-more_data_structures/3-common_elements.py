#!/usr/bin/python3
def common_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    n_ls = []
    for el in s1:
        for els in s2:
            if el == els:
                n_ls.append(el)
    return set(n_ls)
