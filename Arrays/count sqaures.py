"""
Consider a sample space S consisting of all perfect squares 
starting from 1, 4, 9 and so on. You are given a number N, you have to
output the number of integers less than N in the sample space S.

"""

# the commented code is my solution which gave me TLE (its right tho) and the uncommented one is the answer LOL.
class Solution:
    def countSquares(self, N):
        
        # count=0
        
        # for i in range(1,round(N**0.5)):
        #     if i**2 <N:
        #         count+=1
        #     else:
        #         break
            
            
        # return count    
        
        return int((N-1)**0.5)
