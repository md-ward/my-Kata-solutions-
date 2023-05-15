# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"
def DNA_strand(dna:str)->str:
    temp=''
    for i in dna:
        if i=='A':
            temp+='T'
        if i=='T':
            temp+='A'
        if i =='G':
            temp+='C'
        if i=='C':
            temp+='G'
    return temp                    
    
print(DNA_strand('ATTGC'))

    