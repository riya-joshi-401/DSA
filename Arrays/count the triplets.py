# two pointers approach , mine !!

class Solution:
	def countTriplet(self, arr, n):
	    count=0
	    arr=list(set(arr))
	    arr.sort()
	    for i in range(0,n):
	        start=0
	        end=n-1
	        while start<end:
	            if arr[start]+arr[end]==arr[i]:
	                count+=1
	                start+=1
	                end-=1
	            elif arr[start]+arr[end]<arr[i]:
	                start+=1
	            else:
	                end-=1
	                
	    return count
	        
      
      
# other beautiful approach i found, using map
from collections import defaultdict
class Solution:
	def countTriplet(self, arr, n):
	    
	    count=0
	    arr=list(set(arr))
	   
	    d=defaultdict(lambda:0)
	   
	    for i in arr:
	        d[i]+=1
	       
	    for i in range(n):
	        for j in range(i+1,n):
	            if d[arr[i]+arr[j]]!=0:
	                count+=1
	    return count
