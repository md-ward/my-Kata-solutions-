def take_while(arr, pred_fun):
    arr = set(arr)
    temp = []
    for i in arr:
        if pred_fun(i):
            temp.append(i)
    return temp

