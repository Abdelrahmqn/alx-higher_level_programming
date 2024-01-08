#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    for s in my_string:
        if s != 'c' and s != 'C':
            new_s += s
        return new_s
