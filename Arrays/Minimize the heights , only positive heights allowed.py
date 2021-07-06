class Solution:
    def getMinDiff(self, arr, n, k):
        
        # sorrt the array
        arr.sort()
        
        # initialize the variables
        diff=arr[n-1]-arr[0]
        
        # loop
        for i in range(1,n): # since we are writing i-1 in one place below we have to start loop from 1 , otherwise 0-1 will be -1.
            if arr[i]>=k: # for checking that whether after substractong the answer will be positive or not
                
                max_val=max(arr[i-1]+k,arr[n-1]-k)  # here inside max first term has i-1 because if it becomes n-1 i.e last element and we add k to it we will get very high number but we want such numbers that we can minimize the diff to large extend
                min_val=min(arr[0]+k,arr[i]-k)
                diff=min(diff,max_val-min_val)
                
