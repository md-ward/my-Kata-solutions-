import math


def strong_num(number):
    sum = 0
    for i in str(number):
        sum += math.factorial(int(i))
    if sum == number:
        return "STRONG!!!!"
    return "Not Strong !!"



