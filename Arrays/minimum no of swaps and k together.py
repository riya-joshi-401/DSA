def minSwap (arr, n, k) : 
    
    
    good=0 # elements smaller and equal to k
    swaps=float('inf') 
    bad=0  # elements greater than k
    
    
    for i in range(n):
        if arr[i]<=k:
            good+=1
    # this good will be the window size
            
    for i in range(good):
        if arr[i]>k:
            bad+=1
    # we get the number of elements greater k in the first window 
    
    # two pointers which are actually the indcies of the first and last element of the window
    i=0
    j=good-1 
    
    while j<n:
        swaps=min(swaps,bad) # minimum swaps
        j+=1 # move j ahead
        if j<n and arr[j]>k: 
            bad+=1 
        if i<n and arr[i]>k:
            bad-=1 # we are doing this because the window will slide or move ahead after that so that element will no longer be a part of that widnow and IMPORTANTLY chances will be that that might have been already been counted in earlier window where that element was the last element in that window , hence we gotta subtarct one from p
        i+=1 # move i ahead
