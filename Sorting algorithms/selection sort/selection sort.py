"""
1. Find the minimum value in the list
2. Swap it with the value in the current position
3. Repeat this process for all the elements until the entire array is sorted

"""

for i in range(0,n-1):
    min=i 
    for j in range(i+1,n):
        if A[j]<A[min]:
            min=j 
    # swap elements
    A[min],A[i]=A[i],A[min]
