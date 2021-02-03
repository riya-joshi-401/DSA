
def binarysearch(self, arr, n, k):
		
	l=0
	r=n-1
		
    while l <= r: 
  
        mid = l + (r - l) // 2
              
        # Check if x is present at mid 
        if arr[mid] == k: 
            return mid 
      
        # If x is greater, ignore left half 
        elif arr[mid] < k: 
            l = mid + 1
      
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # if we reach here, then the element was not present 
    return -1

