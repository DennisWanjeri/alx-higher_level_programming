#!/usr/bin/python3

"""prints x elements of a list"""
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while(x > 0):
            print("{}".format(my_list[x]), end="")
            x -= 1
            i += 1
    except IndexOutOfRange:
        print("index out of range")
    finally:
        return i
