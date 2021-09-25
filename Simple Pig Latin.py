def pig_it(text):
    x=text.split()
    l=[]
    for i in x:
        if(i not  in ['!','?']) :
            f=i.replace( i[0],i[1:]+i[0]+'ay')
            f=f[0:len(i)+2]
            l.append(f)
        if i in ['!','?']:
            l.append(i)
    return str(' '.join(l))