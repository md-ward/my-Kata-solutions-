
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def mixed_fraction(s):
    arr = s.split('/')
    num, den = [int(i) for i in arr]
    if den == 0:
        raise ZeroDivisionError
    else:
        if num % den == 0:
            return str(num//den)
        elif abs(num) < abs(den):
            return str(num//gcd(num, den)) + '/' + str(den//gcd(num, den))
        else:
            if (num < 0 and den > 0) or (num > 0 and den < 0):
                return '-' + str(abs(num)//abs(den)) + ' ' + str((abs(num) % abs(den))//gcd(abs(num), abs(den))) + '/' + str(abs(den)//gcd(abs(num), abs(den)))
            else:
                return str(num//den) + ' ' + str((num % den)//gcd(num, den)) + '/' + str(den//gcd(num, den))