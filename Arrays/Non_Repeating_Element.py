# Find the first non-repeating element in a given array arr of N integers.
# Note: Array consists of only positive and negative integers and not zero.

from collections import Counter

class Solution:
    def firstNonRepeating(self, arr, n): 
        c=Counter(arr)
        
        for i in arr:
            if c[i]==1:
                return i
                break
