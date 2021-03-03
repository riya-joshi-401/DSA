import sys

def minAbsSumPair(arr, n):
    
    # variables to keep track of minimum sum 
    min_sum = sys.maxsize
  
    # left and right index variables 
    l = 0
    r = n-1
  
    # variable to keep track of the left and right pair for min_sum 
    min_l = l
    min_r = n-1 
  
    # Array should have at least two elements
    if(n < 2): 
        print("Invalid Input")
        return
    
    # sort the elements
    arr.sort()
    
    
    while(l < r):

        curr_sum = arr[l] + arr[r]
      
        # If abs(curr_sum) is less then update the result items
        if(abs(curr_sum) < abs(min_sum)):
            min_sum = curr_sum
            min_l = l
            min_r = r
        
        if(curr_sum < 0):
            l+=1
        else:
            r-=1
      
    print(" The two elements whose sum is minimum are:", 
              arr[min_l],"and", arr[min_r])

  
arr=[1, 60, -10, 70, -80, 85]
n=len(arr)   
minAbsSumPair(arr, n)    
    
