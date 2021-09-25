
def reversed_string(string):
    reversed_string = string[::-1]
    return reversed_string
def check_palindrome_1(string):
    reversed_string = string[::-1]
    status=1
    if(string!=reversed_string):
        status=0
    return status    
    
def isPrime(N): 
    return all(N%p for p in range(3,int(N**0.5)+1,2)) if N>2 and N&1 else N==2
def backwards_prime(start, stop):
    primes=[]
    if start>stop:return []
    for i in range(stop,start,-1):
        if isPrime(i)and  not check_palindrome_1(str(i)) and  isPrime(int (reversed_string(str(i)))):
            primes.append(i)
    return sorted(primes) 

        

    
          


        