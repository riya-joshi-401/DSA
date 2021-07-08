class Solution:
    def sb(self, a, n, x):
        
        
        summ=0
        lenn=float('inf')
        start=0
        
        for i in range(n):
            
            summ+=a[i]
            
            while summ>x and start<=i:
                
                summ-=a[start]
                lenn=min(lenn,i-start+1)
                start+=1
            
        return lenn        
