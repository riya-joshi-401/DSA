# Time complexity : O(logn)
# Space complexity : O(1)

""" We divide the array in two halves , if the middle element is the element that we were looking for then our search completes , 
else we check whether the element we are looking is smaller or bigger than the middle element , then accordingly we split the  part
into two halves again and this process goes on untill we find the element if present else return -1  """

def binarysearch(self, arr, n, k):
	
	l=0
	r=n-1
		
	while l <= r: 
  
		mid = l + (r - l) // 2  # mid = (low + high )//2 = low + (high-low)//2

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

