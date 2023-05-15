from string import ascii_lowercase
import numpy as np
from collections import Counter

def find_the_key(message, code):
    letters=ascii_lowercase
    nums=range(1,27)
    letters_map=dict(zip(letters,nums))
    temp=[]
    for i in message:
        temp.append(letters_map[i])
    x=np.subtract(code,temp)
    count=Counter(x)
    print(temp,x)
find_the_key("scout", [20, 12, 18, 30, 21])    
find_the_key("nomoretears",  [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20])
find_the_key("masterpiece", [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])