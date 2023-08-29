#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write("Exception: {}\n".format(str(err)))
        return False
    except TypeError as err:
        sys.stderr.write("Exception: {}\n".format(str(err)))
        return False
    return True
value = 89.9
print(safe_print_integer_err(value))