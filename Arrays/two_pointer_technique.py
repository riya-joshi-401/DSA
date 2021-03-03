def two_pointer_technique(A,x):
    
    # A must be sorted , if not : sort it
    
    n=len(A)
    
    # first pointer
    i = 0
 
    # second pointer
    j = n-1
 
    while i<j:
    
        # If we find a pair
        if (A[i] + A[j] == x):
            return 1
 
        # If sum of elements at current pointers is less, we move towards higher values by doing i++
        elif (A[i] + A[j] < x):
            i+=1
 
        # If sum of elements at current pointers is more, we move towards lower values by doing j--
        else:
            j-=1
    
    
    return 0
            
    
   
A=[10,20,35,50,75,80]
x=70 # value to search
print(two_pointer_technique(A,x)) # 1: pair found , 0: not found
    
