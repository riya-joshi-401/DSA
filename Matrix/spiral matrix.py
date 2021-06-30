class Solution:
    
    
    def spirallyTraverse(self,a, n, m): 
        
        ans = []
        
        left, right = 0, m
        top, bottom = 0, n
        
        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                ans.append(a[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                ans.append(a[i][right - 1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
                
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                ans.append(a[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                ans.append(a[i][left])
            left += 1
        
        
        return ans     
