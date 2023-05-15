def pyramid(n):
    if n==0:
        return []
    temp=[]    
    for i in range(n):
        temp.append([1 for x in range(0,i+1)])
    return temp
print(pyramid(1))        
