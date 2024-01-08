#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 2 - len(tuple_a)
    b = 2 - len(tuple_b)
    if a < 0:
        return tuple_a
    elif b < 0:
        return tuple_b
    tuple_a += (0,) * a
    tuple_b += (0,) * b

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return res