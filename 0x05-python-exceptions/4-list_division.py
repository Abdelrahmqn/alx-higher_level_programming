#!/usr/bin/python3
# how to divide two lists?
# ==>
def list_division(my_list_1, my_list_2, list_length):
    res = []
    try:
        for i in range(list_length):
            if i < len(my_list_1) and i < len(my_list_2):
                try:
                    res = my_list_1[i] / my_list_2[i]
                    res.append(res)
                except ZeroDivisionError:
                    print("division by 0")
                    res.append(0)
                except (TypeError, ValueError):
                    print("wrong type")
                    res.append(0)
            else:
                print("out of range")
                res.append(0)
    finally:
        print("{}".format(res))
    return res