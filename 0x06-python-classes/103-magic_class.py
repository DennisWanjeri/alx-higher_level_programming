#!/usr/bin/python3
"""class magicClass"""
from math import pi


class MagicClass:
    """class magicClass derived from bytecode"""
    def __init__(self, radius=0):
        """magic class initialization"""
        self.radius = radius

    @property
    def radius(self):
        """returns the value of radius"""
        return self._MagicClass__radius

    @radius.setter
    def radius(self, radius):
        """radius validation and assignment"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius

    def area(self):
        """returns area of a circle"""
        return (2 * pi * (self._MagicClass__radius ** 2))

    def circumference(self):
        return (2 * pi * self._MagicClass__radius
