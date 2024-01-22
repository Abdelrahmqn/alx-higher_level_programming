#!/usr/bin/python3
# how to divide two lists?
# ==>
def list_division(my_list_1, my_list_2, list_length):
    list_length = []
    res = []
    try:
        list_length = res.append(my_list_1[i] / my_list_2[i])
        print("{}".format(res))
        return len(list_length)
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
        return 0
    finally:
        print("{}".format(res))