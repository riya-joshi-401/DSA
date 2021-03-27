# Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

from collections import Counter

class Solution:
    def duplicates(self, arr, n): 
        
    	counter=Counter(arr)
    	li=[]
    	
    	for i in counter.keys():
    	    if counter[i]>1:
    	        li.append(i)
    	        
    	if len(li)==0:
    	    return [-1]
    	else:
    	    li.sort()
    	    return li
