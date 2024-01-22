#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list[:x]:
            if isinstance(my_list, int):
                print("{:d}".format(i))
        return i
    except Exception:
        return 0