

def partlist(arr):

    temp = []
    for i in range(len(arr)):
        temp.append((' '.join(arr[:i+1]), ' '.join(arr[i+1:])))
    temp.pop()
    return temp


a = ["az", "toto", "picaro", "zone", "kiwi"]

print(partlist(a))
