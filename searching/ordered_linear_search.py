# Time complexity : O(n)
# Space complexity : O(1)

# If array is already sorted , then in many cases , we don't have to scan the entire array to check if element is present or not

int OrderedLinearSearch( int A[] , int n , int data ):
  for i in range(0,n):
    if A[i]==data:
      return i
    elif A[i]>data:
      return -1
  return -1
