class Solution:
  
    def sortArray(self, nums: List[int]) -> List[int]:
      
        if len(nums) <= 1:
            return nums
          
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        self.sortArray(left)
        self.sortArray(right)
        return self.merge_two_list(left, right, nums)
    
    def merge_two_list(self, a, b , arr):
      
        len_a = len(a)
        len_b = len(b)
        i = j= k = 0
        while i < len_a and j < len_b:
            if a[i] <= b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
            
        
        while i < len_a:
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len_b:
            arr[k] = b[j]
            j += 1
            k += 1
        return arr 
