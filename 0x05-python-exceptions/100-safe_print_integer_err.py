#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write("ValueError\n")
        return False
    except TypeError as err:
        sys.stderr.write("TypeError\n")
        return False
    return True
