"""
Algorithm : 
(1)Sort the given array.
(2)Loop over the array and fix the first element of the possible triplet, arr[i].
(3) Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum, 
    - If the sum is smaller than the required sum, increment the first pointer.
    - Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
    - Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.
    
Time complexity : O(n**2)
Space complexity : O(1)
"""


def find3Numbers(A, arr_size, sum): 
  
    # Sort the elements  
    A.sort() 
  
    # Now fix the first element one by one and find the other two elements  
    for i in range(0, arr_size-2): 
      
  
        # To find the other two elements, start two index variables from two corners of the array and move them toward each other 
          
        # index of the first elementin the remaining elements 
        l = i + 1 
          
        # index of the last element 
        r = arr_size-1 
        while (l < r): 
          
            if( A[i] + A[l] + A[r] == sum): 
                print("Triplet is", A[i],  
                     ', ', A[l], ', ', A[r]); 
                return True
              
            elif (A[i] + A[l] + A[r] < sum): 
                l += 1
            else: # A[i] + A[l] + A[r] > sum 
                r -= 1
  
    # If we reach here, then  no triplet was found 
    return False
  
