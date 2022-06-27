def incrementer(nums :list):
        temp=[]
        numbers=enumerate(nums,1)
        for i ,j in numbers:
            
            temp+=[(i+j)%10]
        return temp




temp=[4, 6, 9, 1, 3]  

print(incrementer(temp))