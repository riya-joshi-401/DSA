# time complexity : O(n)
# space complexity : O(1) 

# unordered linear search means the array is not sorted so we have to search the entire array to check if th element is preent or not .

int UnOrderedLinearSearch(int A[] , int n , int data):
  for i in range(0,n):
    if A[i]==data:
      return i
      
  return -1
  
