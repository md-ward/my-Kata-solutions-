def interlockable(a, b):

    a = bin(a)[2:]
    b = bin(b)[2:]
    dif = abs(len(a)-len(b))
    print(dif, a, b)
    if len(a) == min(len(a), len(b)):

        num1 = '0'*dif+a
        num2 = b
    else:
        num2 = '0'*dif+b
        num1 = a

    print(num1, num2, len(num1), len(num2))
    for i in range(len(num1)-1, -1, -1):
        if num1[i] == num2[i] == '1':
            return False
        print(num1[i], num2[i], i)
    return True


print(interlockable(1140, 4367))


n1 = '10001110100'
n2 = '1000100001111'
n3 = bin(1140)[2:]
n4 = bin(4367)[2:]
print(min(n1, n2))
