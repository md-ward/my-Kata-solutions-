def check_prime(num: int):

    temp = []

    for i in range(1, 10):
        if num % i == 0:
            temp.append(i)
    print(temp)
    if sum(temp) == num+1:
        return True
    elif len(temp) == 1 & temp[0] == 1:
        return True
    else:
        return False


x = [
    100000000000000003,
    100000000000000013,
    100000000000000019,
    100000000000000021
]
for i in x:
    print(check_prime(i))
