#!/usr/bin/python3
def remove_char_at(str, n):
    str_n = ""
    length = len(str)
    for i in range(length):
        if i != n:
            str_n += str[i]
    return str_n
