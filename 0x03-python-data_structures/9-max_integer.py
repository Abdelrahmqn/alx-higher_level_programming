#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    big_num = my_list[0]
    for number in my_list:
        if number > big_num:
            big_num = number
    return big_num
