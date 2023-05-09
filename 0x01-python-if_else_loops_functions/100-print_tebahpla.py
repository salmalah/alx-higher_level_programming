#!/usr/bin/python3
for r in range(ord('z'), ord('a') - 1, -1):
    if r % 2 != 0:
        r = r - 32
    print("{:c}".format(r), end='')
