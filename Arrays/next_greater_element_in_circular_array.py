"""
A space-efficient solution is to deal with circular arrays using the same array. If a careful observation is run through 
the array, then after the n-th index, the next index always starts from 0 so using the mod operator, we can easily access 
the elements of the circular list, if we use (i)%n and run the loop from i-th index to n+i-th index, and apply mod we can 
do the traversal in a circular array within the given array without using any extra space.
Time Complexity: O(n2) 
Auxiliary Space: O(1)
"""

def printNGE(A, n) :
 
    for i in range(n) :
       
        # Initialise k as -1 which is printed when no NGE is found
        k = -1
        for j in range(i + 1, n + i) :
            if (A[i] < A[j % n]) :
                print(A[j % n], end = " ")
                k = 1
                break
 
        if (k == -1) : # Gets executed when no NGE found
            print("-1 ", end = "")
 
# Given array arr[]
arr = [ 8, 6, 7 ]
 
N = len(arr)
 
# Function call
printNGE(arr, N)
 
