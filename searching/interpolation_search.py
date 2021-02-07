# In maths interpolation is a process of constructing new data points within the range of a discrete set of known data points . 
# One often has a number of data points which represent the value of function for a limited number of values of the ndependant variable .
# It is often required to interpolate ( i.e estimate ) the values of that function for an intermediate value of independent variable.

# Linear interpolation :  takes two data points (x1,y1) and (x2,y2)
# y=y1+(y2-y1)*((x-x1)/(x2-x1))   at point (x,y)

# Interpolation algorithm tries to improve binary search
# Data should be ordered and uniformly distributed for best results

# Disadavntge of binary search : it divides the list into two sub lists , but if we already know that the number to searched will be on the 
# beginning or at the end then this dividing rule is useless .

# K = (data - low )/ (high - low)
# this constant K is used to narrow down the space search , in case of binary search this constant is (low+high)/2

# Time complexity : O(n)  , Space complexity : O(1)


int InterpolationSearch( int A[] , int data ):
  low=0
  high=len(A)-1
  
  while low<=high:
    mid= low + (((data - A[low])*(high-low))/(A[high]-A[low]))
    if data==A[mid]:
      return mid+1
    elif data < A[mid]:
      high=mid-1
    else:
      low=mid+1
  return -1

