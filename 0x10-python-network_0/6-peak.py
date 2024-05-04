#!/usr/bin/python3
"""file documentation"""


def find_peak(list_of_integers):
    """function documention finding the peak number
    """
    lenz = len(list_of_integers)
    if not list_of_integers:
        return None

    if (list_of_integers[0] >= list_of_integers[1]):
        if list_of_integers[0] < 0:
            list_of_integers[0] *= -1
        return list_of_integers[0]

    if (list_of_integers[-1] >= list_of_integers[-2]):
        if list_of_integers[1] < 0:
            list_of_integers[1] *= -1
        return list_of_integers[1]

    for i in range(1, lenz - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
           list_of_integers[i] >= list_of_integers[i + 1]):
            if list_of_integers[i] < 0:
                list_of_integers[i] *= -1
            return list_of_integers[i]
    return None

# if not list_of_integers:
#         return None
#     list_of_integers = sorted(list_of_integers)
#     return list_of_integers[-1]
