

def checkOverlap(a: list, b: list) -> bool:
    count = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                count += 1
    return count


def solve(st):

    pre = []
    suf = []
    for i in range(len(st)):
        pre.append(st[:i+1])
        suf.append(st[len(st)-i-1:])
    pre.pop()
    suf.pop()
    suf.reverse()
    temp = []
    t2=[]
    for i in pre:
        if i in suf:
            temp.append(i)
    if checkOverlap(pre,suf)==1:
        t2=temp[:len(temp)//2]
    print('temp is : ', temp)
    print('t2 is :' ,t2)

    print(pre, '\n', suf)
    if temp == []:
        return 0
    return len(max(t2))


print('max length is : ', solve('aaaaaa'))
