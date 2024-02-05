#!/usr/bin/python3
"""inherite a list in sorted.
"""


class MyList(list):
    """nice documentation."""
    def print_sorted(self):
        print(sorted(self))
