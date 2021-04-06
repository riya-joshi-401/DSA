"""
Write a program to count the number of prime nnumbers formed by removing digits from that number from the back.(including the number itself)

eg1- if n=131 , 131 is prime no, 13(by removing 1 from last) is also prime, but 1 is not prime, so ans=2

eg 2 -49999, ans=3 as 49999 is prime, 4999 is prime and 499 is also prime. but 49 and 4 are not prime so ans=3

"""
def isPrime (N):
    if(N == 1): # if N = 1 return 0
        return 0
    i = 2
        # loop from 2 to sqrt(N)
    while(i*i<=N): 
        if(N%i==0): # if N is divisble by any other number return 0 
            return 0
        i+=1
    return 1 # return 1 if N is not divisible by any other number.
    
count=0
n=int(input())
for i in range(len(str(n))):
    if isPrime(int(str(n)[:i+1]))==1:
        count+=1

print(count)
