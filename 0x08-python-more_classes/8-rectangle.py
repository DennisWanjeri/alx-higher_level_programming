#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """Rectangle definition"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width validation and setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0 is True:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height validation and setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0 is True:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__height is 0 or self.__height is 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """print definition"""
        str_r = ""
        if self.__height is 0 or self.__width is 0:
            return str_r

        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]

            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """returns the string representation of the rectangle"""
        rep = "Rectangle({}, {})".format(self.__width, self.__height)
        return rep

    def __del__(self):
        """instance deletion detection"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
