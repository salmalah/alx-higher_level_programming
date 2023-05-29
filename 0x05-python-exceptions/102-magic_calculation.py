#!/usr/bin/python3
def magic_calculation(a, b):
    po = 0
    for ind in range(1, 4):
        try:
            if ind > a:
                raise Exception("Too far")
            po += pow(a, b) / ind
        except:
            po = b + a
            break
     return po
