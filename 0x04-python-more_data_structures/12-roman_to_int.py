#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    diction = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    num = 0
    prev_value = 0
    for char in reversed(roman_string):
        value = diction.get(char, 0)
        if value == 0:
            return 0

        if value < prev_value:
            num -= value
        else:
            num += value
        prev_value = value

    return num
