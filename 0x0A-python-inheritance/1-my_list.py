#!/usr/bin/python3
"""print_sorted"""


class MyList(list):
    """
    MyList
    """
    def print_sorted(self):
        """prints the list in an ascending order"""
        print(sorted(self))
