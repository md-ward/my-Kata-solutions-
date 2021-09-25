import math

def sum_fracts(lst):
    # your code
    if len(lst):
        result = lst[0]
        for i in range(1, len(lst)):
            # add two rationals
            com_div = math.gcd(result[1], lst[i][1])
            result[0] = result[0] * lst[i][1] // com_div + lst[i][0] * result[1] // com_div
            result[1] = result[1] * lst[i][1] // com_div
        com_div = math.gcd(result[0], result[1])
        result[0] //= com_div
        if result[1] == com_div:
            result = result[0]
        else:
            result[1] //= com_div
        return result
    return None