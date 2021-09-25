import numpy as np

def valid_solution(board):
    a=np.array(board)
    
    a1=np.sum(a[0:3,0:3])
    a2=np.sum (a[0:3,3:6])
    a3=np.sum (a[0:3,6:9])
    a4=np.sum (a[3:6,0:3])
    a5=np.sum (a[3:6,3:6])
    a6=np.sum (a[3:6,6:9])
    a7=np.sum (a[6:9,0:3])
    a8=np.sum (a[6:9,3:6])
    a9=np.sum (a[6:9,6:9])
    
    if(a1==45 and a2==45 and a3==45 and a4==45 and a5==45 and a6==45 and a7==45 and a8==45 and a9==45 and all(sum(a)==45)):
        return True
    else:
        return False
#example........................................................    
f=valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])
print(f)
