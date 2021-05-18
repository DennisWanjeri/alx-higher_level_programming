#!/usr/bin/python3
"""class magicClass"""
import math


class MagicClass:
    """class magicClass derived from bytecode"""
    def __init__(self, radius=0):
        """magic class initialization"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returns area of a circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
