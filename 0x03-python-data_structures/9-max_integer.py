#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None

    m_num = my_list[0]

    for nums in my_list[1:]:
        if nums > m_num:
            m_num = nums
            return m_num
