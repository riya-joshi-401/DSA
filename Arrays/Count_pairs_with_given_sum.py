# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

from collections import Counter

class Solution:
    def getPairsCount(self, arr, n, k):
        
        count=0
        pair=0
        
        counter=Counter(arr)
        
        for i in range(n):
            
            if k-arr[i] in counter.keys() and k-arr[i]!=arr[i]:
                count+=counter[k-arr[i]]
            elif k-arr[i] in counter.keys() and k-arr[i]==arr[i]:
                count+=counter[k-arr[i]]
                pair+=1
                
        return (count-pair)//2
