class Solution:
    
    def leaders(self, arr, n):
        leader_count=0
        maxx=float('-inf')
        li=[] 
        
        for i in range(n-1,-1,-1):
            if arr[i]>=maxx:
                maxx=arr[i]
                li.append(arr[i])
                
                
        return li[::-1]
