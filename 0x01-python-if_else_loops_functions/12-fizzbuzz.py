#!/usr/bin/usr
def fizzbuzz():
    for i in range (1 ,101):
        if (i == 100):
            print("Buzz")
            break
        elif i % 15 == 0:
            print("FizzBuzz ", end = "")
        elif i % 3 == 0:
            print("Fizz ", end = "")
        elif i % 5 == 0:
            print("Buzz ", end = "")
        else:
            print("{} ".format(i), end = "")
