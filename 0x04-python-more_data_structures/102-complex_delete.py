#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    if value not in a_dictionary:
        return a_dictionary
    else:
        if value in new:
            del new[value]
    return new