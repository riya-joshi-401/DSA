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
            
            # loc is partitioning index, arr[loc] is now at right place.
            loc=self.partition(arr,low,high)
            
            # Separately sorting elements before and after partitioning index.
            self.quickSort(arr,low,loc-1)
            self.quickSort(arr,loc+1,high)
    
    # This function that takes last element as pivot, places the pivot element at 
    # its correct position in sorted list, and places all smaller elements
    # to left of pivot and all greater elements to right of pivot.
    def partition(self,arr,low,high):
        
        pivot = arr[high] # Picking the pivot.
        i= low-1 # Index of smaller element and indicates the right position of pivot found so far.
        for j in range(low,high):
            # If current element is smaller than or equal to pivot we increment
            # the value of i and swap the values at ith and jth index.
            if arr[j]<=pivot:
                i+=1
                # Swapping of values at ith and jth index.
                arr[i],arr[j]=arr[j],arr[i]
        # At last, swapping of value at ith and the last index which was
        # selected as pivot.        
        arr[i+1],arr[high]=arr[high],arr[i+1]
        # returning the partitioning index. 
        return i+1
        
