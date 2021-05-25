#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """prevents user from dynamically creating new instance
    attribute if new instance is not first_name"""
    __slots__ = ["first_name"]
