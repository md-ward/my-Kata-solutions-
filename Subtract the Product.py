

import numpy


def subtractProductAndSum(n: int) -> int:
    temp = str(n)
    nums = []

    for i in range(len(temp)):
        nums.append(int(temp[i]))

    mul = numpy.prod(nums)
    add = sum(nums)
    return mul-add


print(subtractProductAndSum(4421))
