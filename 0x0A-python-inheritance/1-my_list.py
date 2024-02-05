#!/usr/bin/python3
"""inherite a list in sorted.
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
