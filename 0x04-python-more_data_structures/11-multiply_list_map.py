#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new = [list(map(lambda o: o * number, i)) for i in my_list]
    return new
