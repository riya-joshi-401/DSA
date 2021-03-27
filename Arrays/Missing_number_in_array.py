# Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.
def MissingNumber(array,n):
    
    li=[i for i in range(1,n+1)]
    
    new_li=set(li).difference(set(array))
    
    list(new_li).sort()
    
    return list(new_li)[0]
    
