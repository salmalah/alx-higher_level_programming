#!/usr/bin/python3
def magic_calculation(a, b):
    po = 0
    for ind in range(1, 3):
        try:
            if ind > a:
                raise Exception('Too far')
            else:
                po += (a ** b) / i
        except:
            po = b + a
            break
    return po
