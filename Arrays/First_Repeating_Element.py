# Given an array arr[] of size n, find the first repeating element. The element should occurs more than once and the index of its first occurrence should be the smallest.
from collections import Counter

class Solution:
    
    def firstRepeated(self,arr, n):
        
        store=Counter(arr)
        
        for i in arr:
            if store[i]>1:
                return arr.index(i)+1
                break
        return -1      
