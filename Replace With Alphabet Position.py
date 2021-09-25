def alphabet_position(text):
    a=text.lower()
    z=""
    x=""
    for i in a:
        if(i>='a' and i<='z'):
            z+=str(ord(i)-ord('a')+1)+" "
    x=z[0:len(z)-1]
    return x