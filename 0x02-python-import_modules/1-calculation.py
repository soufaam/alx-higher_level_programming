#!/usr/bin/python3
_add_0 = __import__('add_0')
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, _add_0.add(a, b)))
