class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		index=-1
		summ=0
		for i in range(n):
		    if sum(arr[i])>summ:
		        summ=sum(arr[i])
		        index=i
		        
		return index
