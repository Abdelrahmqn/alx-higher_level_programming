#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            res = a / b
            return res
        else:
            return None
    except ZeroDivisionError:
        return None
    finally:
        try:
            print("Inside result: {}".format(res))
        except Exception:
            print("Inside result: None")
            return None
