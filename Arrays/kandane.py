
# old solution 

"""

def kandane(A):
    
    n=len(A)
    local_max=0
    global_max=float('-inf')
    
    for i in range(n):
        
        local_max=max(A[i],A[i]+local_max)
        
        if local_max>global_max:
            global_max=local_max
            
    return global_max
    

    
A=[-2,1,-3,4,-1,2,1,-5,4]
ans=kandane(A)
print("Maximum sum of subarray : ",ans)

"""

class Solution:
    
    def maxSubArraySum(self,a,size): 
           
        max_so_far = float('-inf')
        max_ending_here = 0
        
        #Iterating over the array. 
        for i in range(0, size): 
            #Updating max sum till current index.
            max_ending_here = max_ending_here + a[i]
            
            #Storing max sum so far by choosing maximum between max 
            #sum so far and max sum till current index.
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
        
            #If max sum till current index is negative, we do not need to add
            #it to result so we update it to zero.
            if max_ending_here < 0: 
                max_ending_here = 0   
        
        #returning the result.
        return max_so_far
