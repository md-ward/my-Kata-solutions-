def tower_builder(n_floor):
    a = '*'
    b = 1
    c= 0
    result = []
    num=range(1, n_floor+1)

    # * to increment by odd number
    for _ in num:
        c = a
        result.append(c)
        a += str('**')
        temp=[]
    for i in result[:-1]:
        
        t=len(result[-1])-len(i)
        t2=t//2        
        temp.append('{}{}{}'.format(' '*t2,i,' ' *t2))
    temp.append(result[-1])
    return temp    
#example................
f=tower_builder(5)
for i in f:
    print(i)