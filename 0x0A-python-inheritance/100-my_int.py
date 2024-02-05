#!/usr/bin/python3
"""defines a class that is not equal the true
"""


class MyInt(int):
    """return the opposite of the truth
    """

    def __eq__(self, num):
        """return super__eq__(other)
        """
        return self.real is not num

    def __ne__(self, num):
        """return self.real isn't num
        """
        return not super().__ne__(num)
