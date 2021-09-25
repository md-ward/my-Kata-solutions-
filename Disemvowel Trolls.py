def disemvowel(s):
    va=''
    for i in s:
        if i in ['a','u','e','i','o','A','U','E','I','O']:
            continue
        va+=i
    return va 