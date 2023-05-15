from collections import Counter


def is_isogram(string: str):
    ctn = Counter(string.lower())
    vals=ctn.values()
    for i in vals:
        if i>1:
            print(i)
            return False

    return True      
print(is_isogram(''))
