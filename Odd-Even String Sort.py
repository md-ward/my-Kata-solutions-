def sort_my_string(s):


    temp=enumerate(s)
    odd=''
    even=''
    for i ,j in temp:
        if i==0 or i%2==0:
            even+=j
        else: odd+=j
    return '{} {}'.format(even,odd)       