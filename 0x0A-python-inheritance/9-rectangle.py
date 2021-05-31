#!/usr/bin/python3
"""rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """
        constructor
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def __str__(self):
        """print representation"""
        string = "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
        return string
