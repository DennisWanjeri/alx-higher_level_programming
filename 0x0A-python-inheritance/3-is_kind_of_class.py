#!/usr/bin/python3
"""
3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class 
    """
    if isinstance(obj, a_class):
        return True
    return False
