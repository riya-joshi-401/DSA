# time complexity : O(logN) , space complexity : O(1)
class Solution:
    def trailingZeroes(self, N):

        if N<5:
            return(0)
        else:
            i=5
            c=0
            while (N//i !=0):
                c=N//i + c
                i=i*5
            return(c)
          
# my solutions that gave TLE but will work if O(N) space is allowed ..hope :)

import math

class Solution:
    def trailingZeroes(self, N):
        fact=math.factorial(N)
        li=list(map(int,str(fact)))
    	count=0
    	
    	for i in li[::-1]:
    	    if i==0:
    	        count+=1
    	    else:
    	        break
    	return count
    

import math

class Solution:
    def trailingZeroes(self, N):
        fact=math.factorial(N)
    	count=0
    	
    	while fact>0:
    	    
    	    if fact%10==0:
    	        fact=int(fact//10)
    	        count+=1
    	    else:
    	        break
    	    
    	return count

