class Solution:
    def threeSumClosest (self, arr, target):
        
        ans=float('-inf') # we have to output the maximum closest sum here
        currsum=0
        n=len(arr)
        
        arr.sort() # sort to improve efficiency of algorithm :)
        
        for i in range(n):
            
            # use two pointers
            
            start=i+1 # to avoid repeating the ith element obvio dumbo :)
            end=n-1
            
            while start<end: 
                
                currsum=arr[i]+arr[start]+arr[end] # current sum
                
                if abs(target-ans)>abs(target-currsum):
                    ans=currsum # because we want closest sum :)
                    
                elif abs(target-ans)==abs(target-currsum):
                    ans=max(ans,currsum) # we want maximum (closest) sum among all the answers
                
                if target>currsum: # increasing the sum
                    start+=1
                    
                else: # decreasing the sum
                    end-=1
                    
                    
        return ans
