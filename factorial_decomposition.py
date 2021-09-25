import math 
def isPrime(N): 
    return all(N%p for p in range(3,int(N**0.5)+1,2)) if N>2 and N&1 else N==2
def decomp(n):
    temp=math.factorial(n)
    list=[]
    for i in range(n+1):
        if(isPrime(i)):
            list.append(i)
    count=0
    s=''
    for i in list:
        while temp%i==0:
            temp = temp//i
            count+=1
        if count==1:
            s+="{} * ".format(i)
        else:s+="{}^{} * ".format(i,count)   
        count=0    
    return s[:-3]
print(decomp(25))


                
    