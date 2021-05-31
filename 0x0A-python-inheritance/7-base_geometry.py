#!/usr/bin/python3
"""6-base_geometry.py"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """Not implemented exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
