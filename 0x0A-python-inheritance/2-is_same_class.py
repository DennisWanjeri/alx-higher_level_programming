#!/usr/bin/python3
"""2-is_same_class.py"""


def is_same_class(obj, a_class):
    """tests whether an object is an instance of a specified class"""
    if type(obj) == a_class:
        return True
    return False
