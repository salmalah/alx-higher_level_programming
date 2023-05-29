#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("Nove u <3 so much")
except NameError as ne:
    print(ne)

