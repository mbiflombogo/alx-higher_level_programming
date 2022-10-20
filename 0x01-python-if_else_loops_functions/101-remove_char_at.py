#!/usr/bin/python3
def remove_char_at(str, n):
    s = str[:]
    return (s[:n] + s[n+1:])
