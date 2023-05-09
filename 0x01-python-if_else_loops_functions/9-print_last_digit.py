#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        l_digit = (number % -10) * -1
    else:
        l_digit = number % 10
    print("{}".format(l_digit), end='')
    return l_digit
