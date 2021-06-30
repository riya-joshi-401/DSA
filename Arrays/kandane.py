class Solution:
    
    def maxSubArraySum(self,a,size):
        
        maxSum=float('-inf')
        currSum=0
        
        for i in range(0,size):
            
            currSum=currSum + a[i]
            
            if maxSum<currSum:
                maxSum=currSum
                
            if currSum<0:
                currSum=0
                
        return maxSum
