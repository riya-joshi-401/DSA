class Solution:	
    
	def reverseInGroups(self, arr, n, k):
		
		temp=0 # to keep track of groups
		start=0 # start pointer
		last_index=0 # last pointer
		
		
		for i in range(n):
		    if temp==k:
		        arr[start:i]=arr[start:i][::-1]
		        last_index=i
		        start=i
		        temp=1
		    else:
		        temp+=1
		        
		if last_index<n-1: # after reversing k groups of elements if elements are still remaining then irrespective of whether k group is there or not reverse them
		    arr[last_index:]=arr[last_index:][::-1]
