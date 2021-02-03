
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
