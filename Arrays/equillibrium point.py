class Solution:
   
    def equilibriumPoint(self,A, n):
        
        summ=0
        currsum=0
        
        for i in A:
            summ+=i
            
        for i in range(n):
            if currsum==summ-currsum-A[i]:
                return i+1
            else:
                currsum+=A[i]
            
        return -1    
