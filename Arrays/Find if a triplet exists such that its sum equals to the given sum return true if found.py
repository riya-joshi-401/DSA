# Time complexity: O(n**2)
# Space complexity: O(1)

class Solution:
     
    
    def find3Numbers(self,arr, n, X):
        
       
        arr.sort() # sorting first , coz its a must :-)
       
        for i in range(n):
            
            start=i+1
            end=n-1
            
            while start < end:
           
                if arr[i]+arr[start]+arr[end]==X:
                    return 1
                    break
                elif arr[i]+arr[start]+arr[end]<X:
                    start+=1
                elif arr[i]+arr[start]+arr[end]>X:
                    end-=1
                
        return 0   
