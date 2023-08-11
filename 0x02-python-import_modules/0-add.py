#!/usr/bin/python3
if __name__ == "__main__":
    adding = __import__('add_0')
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, adding.add(a, b)))
