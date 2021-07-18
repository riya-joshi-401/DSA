for i in range(1,n):
    
    v=A[i]
    j=i
    
    while(A[j-1]>v and j>=1):
        
        A[j]=A[j-1]
        j-=1 
        
    A[j]=v
