# Arithmetic progression

"""

If ‘a’ is the first term and ‘d’ is the common difference,
(1) nth term of an AP = a + (n-1) d
(2) Arithmetic Mean = Sum of all terms in the AP / Number of terms in the AP
(3) Sum of ‘n’ terms of an AP = 0.5 n (first term + last term) = 0.5 n [ 2a + (n-1) d ]

"""

# naive solution
def checkIsAP(arr, n):
    if (n == 1): return True
  
    # Sort array
    arr.sort()
  
    # After sorting, difference between
    # consecutive elements must be same.
    d = arr[1] - arr[0]
    for i in range(2, n):
        if (arr[i] - arr[i-1] != d):
            return False
  
    return True
  
# Driver code
arr = [ 20, 15, 5, 0, 10 ]
n = len(arr)
print("Yes") if(checkIsAP(arr, n)) else print("No")
