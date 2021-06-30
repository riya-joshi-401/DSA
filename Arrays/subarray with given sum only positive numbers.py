class Solution:
    def subArraySum(self,arr, n, s): 
        
        # initialize
        current_sum=0
        start=0
        i=0
        
        # Add elements one by one to current_sum and if curren_sum exceeds the sum , the remove starting element
        for i in range(0,n+1):
            
            # if current_sum exceeds the sum and then keep on removing elements from starting till it becoms equal to sum
            while current_sum > s and start < i-1:
                
                current_sum-=arr[start]
                start+=1
                
            # if current_sum becomes equal to sum, then return the elements
            if current_sum==s:
                return [start+1,i]
                break
                
            if i<n:
                current_sum+=arr[i]
            
        return [-1]
