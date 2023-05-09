#!/usr/bin/python3
def uppercase(str):
    for car in str:
        if ord(car) >= 97 and ord(car) <= 122:
            car = chr(ord(car) - 32)
        print("{}".format(car), end='')
    print()

