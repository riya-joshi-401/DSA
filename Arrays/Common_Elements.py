# Given two lists V1 and V2 of sizes n and m respectively. Return the list of elements common to both the lists and return the list in sorted order. 
# Duplicates may be there in the output list.

from collections import Counter

class Solution:
    def common_element(self,v1,v2):
        
        li=[]
        v1_c=Counter(v1)
        v2_c=Counter(v2)
        
        for i in v1_c:
            
            if i in v2_c:
                
                m=min(v1_c[i],v2_c[i])
                li+=[i]*m
                
        li.sort()
        return li
