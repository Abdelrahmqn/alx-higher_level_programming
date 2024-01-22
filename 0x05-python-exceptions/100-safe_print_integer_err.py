#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
        else:
            return False
    except ValueError:
        return False
