#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """inherits from int, has == and != inverted"""

    def __eq__(self, value):
        """overiding == operator"""
        return self.real != value

    def __ne__(self, value):
        """overriding != operator"""
        return self.real == value
