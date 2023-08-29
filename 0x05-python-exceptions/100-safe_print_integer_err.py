#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write("Exception: Unknown format code\
 'd' for object of type 'str'\n")
        return False
    except TypeError as err:
        sys.stderr.write("TypeError: unsupported format string passed \
to NoneType.__format__'\n")
        return False
    return True
