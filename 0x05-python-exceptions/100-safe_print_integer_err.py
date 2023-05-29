#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except  Exception as m:
        print("Exception: {}".format(m), file=sys.stderr)
        return False
