#!/usr/bin/python3
"""add attribute"""


def add_attribute(obj, attribute, value):
    """adds an attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
