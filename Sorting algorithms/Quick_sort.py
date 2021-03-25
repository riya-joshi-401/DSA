# Divide and conquer algorithm technique
# Also called "partition-exchange sort algorithm"
# comparison based sorting algo
# Uses recursive calls for sorting the elements

"""

Algorithm

The recursive algorithm consists of four steps:
1)If there are one or no elements in the array to be sorted, return.
2)Pick an element in the array to serve as the “pivot” point. (Usually the left-mostelement in the array is used.)
3)Split the array into two parts – one with elements larger than the pivot and the otherwith elements smaller than the pivot.
4)Recursively repeat the algorithm for both halves of the original array.Implementation.

"""

# Time complexity for average / best case : O(nlogn) , worst : O(n**2)

class Solution:
    
    def quickSort(self,arr,low,high):
        
        if low<high:
            
            loc=self.partition(arr,low,high)
            self.quickSort(arr,low,loc-1)
            self.quickSort(arr,loc+1,high)
    
    def partition(self,arr,low,high):
        
        pivot = arr[high]
        i= low-1
        for j in range(low,high):
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
                
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
        
       
