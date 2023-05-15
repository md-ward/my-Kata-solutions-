
def correct(s):
    new=''
    for i in s :
        if i =='0':
            new+="O"
        elif i=='1':
            new+='I'
        elif i=='5' :new+='S'
        else:new+=i
    return new    
print(correct('L0ND0N'))    

def correct(string):
    return string.translate(str.maketrans("501", "SOI"))