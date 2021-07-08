# time complexity : O(n) , space complexity: O(1)

class Solution:
    def subArraySum(self,arr, n, s): 
       
        # initialize
        currsum=0
        start=0
       
        for i in range(n):
            # Add elements one by one to current sum and if curren sum exceeds the sum , then remove starting element
            currsum+=arr[i]
           
            # if current sum exceeds the sum and then keep on removing elements from starting till it becoms equal to sum
            while currsum>s and start<=i:
               
                currsum-=arr[start]
                start+=1
             
            # if current sum becomes equal to sum, then return the elements
            if currsum==s:
                return [start+1,i+1]
                break
            
        return [-1]
