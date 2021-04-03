"""
# A school method based Python3  program to check if a number is prime
def isPrime(n):

    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;

    return True
"""

#Efficient method
# The factors from 2 to sqrt(n) have multiples from sqrt(n)+1 to n.

class Solution:
    def isPrime (self, N):
        if(N == 1): # if N = 1 return 0
            return 0
        i = 2
        # loop from 2 to sqrt(N)
        while(i*i<=N): 
            if(N%i==0): # if N is divisble by any other number return 0 
                return 0
            i+=1
        return 1 # return 1 if N is not divisible by any other number.
    
    # For that 6k-+1 method check : https://en.wikipedia.org/wiki/Primality_test
