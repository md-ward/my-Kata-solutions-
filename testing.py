l = ["black", "blue", "red", "green", "white"]

templist = []
x=0
for item in l[x:]:
    for i in l[1:]:
        if item!=i:
         templist.append([item,i])
    x+=1     
print(templist,'\n\n')    
from itertools import combinations

L = ["black","blue","red","green","white"]

print(list(combinations(L,2)))