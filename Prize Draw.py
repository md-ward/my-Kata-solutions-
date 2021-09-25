def rank(st, we, n):
    import string    
    alph = string.ascii_lowercase
    win_num = []
    names = st.split(',')
    if not st:
        return 'No participants'
    if n>len(names):
        return 'Not enough participants'
    for index,name in enumerate(names):
        
        length = len(name)
        count = sum([alph.index(i)+1 for i in name.lower()])
        win_num.append((length+count)*we[index])    
    result = [(rank,name) for rank,name in zip(win_num,names)]    
    result = sorted(result,key=lambda x:(-x[0],x[1]))
 
    return result[n-1][1]