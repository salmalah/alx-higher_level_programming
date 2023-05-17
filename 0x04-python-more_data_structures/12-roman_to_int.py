#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    diction = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    n = 0
    prev_val = 0
    for char in reversed(roman_string):
        value = diction.get(char, 0)
        if not value:
            return 0
        if value < prev_val:
            n = n - value
        else:
            n = n + value
        prev_val = value
    return n
