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
        sys.stderr.write("Exception: Unknown format code\
 'd' for object of type 'str'\n")
        return False
    return True
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))