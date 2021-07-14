class Solution:
    def productExceptSelf(self, nums, n):
        
        prod=1
        zero=0
        
        for i in nums:
            if i!=0:
                prod=prod*i
            else:
                zero+=1
            
        for i in range(n):
            if zero==1 and nums[i]!=0:
                nums[i]=0
            elif zero==1 and nums[i]==0:
                nums[i]=prod
            elif zero>1:
                nums[i]=0
            elif zero==0:
                nums[i]=prod//nums[i]
            
            
        return nums
