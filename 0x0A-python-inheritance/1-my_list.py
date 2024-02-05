#!/usr/bin/python3
"""inherite a list in sorted.
"""


class MyList(list):
    """inherets from list"""
    def print_sorted(self):
        """print_sorted support to print in sorted order.
        """

        print(sorted(self))
