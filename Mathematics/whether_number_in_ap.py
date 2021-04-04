"""
Q:
Given three integers  'A' denoting the first term of an arithmetic sequence , 'C' denoting the common difference of an arithmetic 
sequence and an integer 'B'. you need to tell whether 'B' exists in the arithmetic sequence or not.

"""

class Solution:
    def inSequence(self, A, B, C):
        
        if A==B:
            return 1
        elif C!=0:
            res=(B-A)%C
            if(res==0 and ( ((B-A)<0 and C<0) or ((B-A)>0 and C>0))):
                return 1
        return 0
        
