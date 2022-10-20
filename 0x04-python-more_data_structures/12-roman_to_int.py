#!/usr/bin/python3
def roman_to_int(roman_string):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) != str or roman_string is None:
        return 0
    total = 0
    adj = 0
    for ch in roman_string:
        total += symbols[ch] if symbols[ch] <= adj else symbols[ch] - adj * 2
        adj = symbols[ch]
    return total
