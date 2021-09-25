def unique_in_order(string):
    temp=[]
    for i in string:
        if len(temp)<1 or i!=temp[len(temp)-1]:
            temp.append(i)
    return temp
