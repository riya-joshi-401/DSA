class Solution:
	def minJumps(self, arr, n):
	    
	    if n==0 or n==1: # if we dont have any element or have only one element so we are at end element only
	        return 0
	    elif arr[0]==0: # if first element is zero itself we cant move further
	        return -1
	    else:
    	    # initialization
    	    max_reach = arr[0]  # maximum index upto which it can go
    	    steps = arr[0]  # number of steps remaining to be completed
    	    jumps=0 # number of jumps
    	    
    	    for i in range(1,n-1): # traversing till second last element
    	        
    	        steps-=1 
    	        max_reach=max(max_reach,arr[i]+i) #  maximum of max reach and current index + its value
    	        if steps==0: # which means we have traversed till our max reach range
    	            jumps+=1 # since we have traversed all the indices upto max reach we by now must have made a jump and have selected ournew max range
    	            steps=max_reach-i # this will be now the new stepsthat we have to take
    	            if steps<=0: # if counter something like array: 2 1 0 3 , where it becomnes impossible to reach end element
    	                return -1
    	                break
    	    return jumps+1 # we start our array from 1st element so we are assuming we are taking first jump but not counting it anywhere so we add + 1 to jumps 
        
        
        # explanation is written by me only , but for understanding this problem i have referred some youtube video ;-)
