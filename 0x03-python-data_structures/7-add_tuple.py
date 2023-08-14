#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 2 and len(tuple_a) == 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
    elif len(tuple_b) < 2 and len(tuple_a) == 2:
        b = tuple_a[1]
        a = tuple_a[0] + tuple_b[0] if len(tuple_b) == 1 else tuple_a[0]
    elif len(tuple_a) < 2 and len(tuple_b) == 2:
        b = tuple_b[1]
        a = tuple_a[0] + tuple_b[0] if len(tuple_a) == 1 else tuple_b[0]
    else:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
    return (a, b)
