#!/usr/bin/python3
def uppercase(str):
    for caractere in str:
        if ord(caractere) >= 97 and ord(caractere) <= 122:
            print("{}".format(chr(ord(caractere)-32)), end='')
    print("");

