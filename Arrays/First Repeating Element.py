from collections import defaultdict

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        flag=False
        
        Map=defaultdict(lambda:0)
        
        for i in arr:
            Map[i]+=1
            
        n_updated=len(set(arr))
            
        for i in range(n_updated):
            if Map[arr[i]]>1:
                flag=True
                return i+1
                break
        
        if flag==False:
            return -1
        
        
    # another same method , i had done it some months ago :)
    
    from collections import Counter

    class Solution:

        def firstRepeated(self,arr, n):

            store=Counter(arr)

            for i in arr:
                if store[i]>1:
                    return arr.index(i)+1
                    break
            return -1      
