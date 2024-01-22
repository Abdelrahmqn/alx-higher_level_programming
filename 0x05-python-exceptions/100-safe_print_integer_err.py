#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
    except Exception:
        print("{}".format(value), file=stderr)
        return False
