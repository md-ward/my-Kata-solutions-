def in_asc_order(arr):
    temp=0
    try:
        for i in range (len(arr)):
            if arr[i]<arr[i+1]:
                temp+=1
    except:
        temp+=1
    print(temp)
    if temp==len(arr):
        return True
    return False                

    
    return bool #(True or false)
print(in_asc_order([1,2,4,7,19])) # returns True
# in_asc_order([1,2,3,4,5]) # returns True
print(in_asc_order([1,6,10,18,2,4,20])) # returns False
# in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order    