# expected time complexity: O(n) , space complexity: O(1)

# My lullu solution ;-)
from collections import Counter

class Solution:
    def findTwoElement( self,arr, n): 
        
        A= list(set([i for i in range(1,n+1)]).difference(set(arr)))[0]
        count = Counter(arr)
        
        for i in count:
            if count[i]==2:
                B=i
                break
    
        return [B,A]
    
    # another easy peasy approach
    def findTwoElement( self,l, n):
      ans=[0]*2
      k=list(set(l))
      ans[1]=((n*(n+1))//2)-sum(k)
      ans[0]=sum(l)-sum(k)
      return(ans)
