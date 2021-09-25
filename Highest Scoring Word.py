import string
def sum(word):
    sum=0
    alph=string.ascii_lowercase
    alphRank=enumerate(alph,1)
    for j ,k in alphRank: 
      for i in word:
          if i==k:
              
              sum+=j            
    return sum            

def high( x)->str:
    score=[]
    words=x.split()
    for i in words:
        score.append(sum(i))
    all=zip(words,score)
    result=sorted(all, key = lambda x: x[1] ,reverse=True)
    return result[0][0]
        
        

