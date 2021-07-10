class Solution:

	def maxProduct(self,arr, n):
	    # Variables to store maximum and minimum product till ith index.
	    minVal = arr[0]
	    maxVal = arr[0]

	    maxProduct = arr[0]

	    for i in range(1, n):

	        # When multiplied by -ve number, maxVal becomes minVal and minVal becomes maxVal.
	        if (arr[i] < 0):
	            maxVal,minVal=minVal,maxVal

	        # maxVal and minVal stores the product of subarray ending at arr[i].
	        maxVal = max(arr[i], maxVal * arr[i])
	        minVal = min(arr[i], minVal * arr[i])

	        # Max Product of array.
	        maxProduct = max(maxProduct, maxVal)

	    # Return maximum product found in array.
	    return maxProduct
	
	:)
