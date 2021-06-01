#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """returns a list of lists representing a pascal triangle of n"""
    if n <= 0:
        return []
    #initialization
    triangles = [[1]]

    while len(triangles) != n:
        #tri points to last list
        tri = triangles[-1]
        lis = [1]
        for i in range(len(tri) -1):
            #pascal algorithm of adding left and right
            lis.append(tri[i] + tri[i + 1])
        lis.append(1)
        triangles.append(lis)
    return triangles
