#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for key, value in dic.items():
        print("{}: {}".format(key, value))
    for key, item in a_dictionary.items():
        a_dictionary[key] = item * 2

    return a_dictionary
