import math


def custom_sqrt(number):
    if number < 0:
        return -math.sqrt(-number)
    return math.sqrt(number)


number = float(input("Enter a number: "))

print(custom_sqrt(number))
