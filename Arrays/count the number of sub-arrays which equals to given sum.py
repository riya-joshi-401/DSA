# Time complexity: O(n)
# Time complexity: O(n) 

from collections import defaultdict 
class Solution:
    
    # Function to find number of subarrays   
    # with sum exactly equal to k.  
    def findSubarraySum(self,arr, n, Sum):  
       
        # Dictionary to store number of subarrays  
        # starting from index zero having   
        # particular value of sum.  
        prevSum = defaultdict(lambda : 0)  
        
        """
        when I call x[k] for a nonexistent key k (such as a statement like v=x[k]), 
        the key-value pair (k,0) will be automatically added to the dictionary, 
        as if the statement x[k]=0 is first executed.
        
        """
        
        res = 0 
        
        # Sum of elements so far.  
        currsum = 0 
        
        for i in range(0, n):   
        
            # Add current element to sum so far.  
            currsum += arr[i]  
        
            # If currsum is equal to desired sum,  
            # then a new subarray is found. So  
            # increase count of subarrays.  
            if currsum == Sum:   
                res += 1         
        
            # currsum exceeds given sum by currsum  - sum. 
            # Find number of subarrays having   
            # this sum and exclude those subarrays  
            # from currsum by increasing count by   
            # same amount.  
            if (currsum - Sum) in prevSum: 
                res += prevSum[currsum - Sum]  
                
        
            # Add currsum value to count of   
            # different values of sum.  
            prevSum[currsum] += 1 
           
        return res 
