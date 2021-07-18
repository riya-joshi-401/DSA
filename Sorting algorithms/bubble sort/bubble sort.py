# using the swap flag variable improves time complexity from o(n**2) to o(n) when the array is already sorted, this flag helps us to skip
# the remaining passes.

class Solution:
    
    def bubbleSort(self,arr, n):
        
        for no_of_pass in range(n-1,-1,-1):
            
            swap = 0
            
            for i in range(no_of_pass):
                
                if arr[i]>arr[i+1]:
                    
                    # swap elements
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    
                    swap=1
                    
            if swap==0:
                break
