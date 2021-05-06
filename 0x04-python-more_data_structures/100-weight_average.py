#!/usr/bin/python3


def weight_average(my_list=[]):
    total = 0
    i = 0
    if len(my_list) == 0:
        return total
    for x in my_list:
        total += (x[0] * x[1])
        i += x[1]
    return (total / i)
