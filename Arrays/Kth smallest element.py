# dumb solution by me , time complexity : O(nlogn) , expected : O(n)
class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        return arr[k-1]
      
 # noice solution by others, time complexity: no idea
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        heapq.heapify(arr)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(arr)
        return ans
