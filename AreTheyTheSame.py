import numpy


def comp(array1, array2):
    if array1==None or array2 ==None:return False
    array1=numpy.abs(array1)
    array2=numpy.abs(array2)
    a=sorted(array1)
    b=sorted(array2)
    
    if len(array1)!=len(array2):return False
    if len(array2)==len(array1)==0:return True
    all=[]
    temp=numpy.power(a,2)
    print(temp)
    for i in range(len(array1)):
        
        if temp[i]==b[i]:
            all.append(True)
        else:all.append(False)    
    
    all=set(all)
    all=list(all)
    if len(all)>1:
        return False
    else:
        return all[0]

a=[-121, -144, 19, -161, 19, -144, 19, -11] 
z=[121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a,z))