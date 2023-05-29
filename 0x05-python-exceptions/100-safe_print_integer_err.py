#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except  except (ValueError, TypeError) as m:
        print("Exception: {}".format(m), file=sys.stderr)
        return False
