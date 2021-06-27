# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/ :  for all methods

# (1) easy to understand and noice approach , no extra space 
# Time complexity : O(nlogn)
def getMedian(ar1, ar2, n):
    i, j = n - 1, 0
 
    # while loop to swap all smaller numbers to arr1
    while(ar1[i] > ar2[j] and i > -1 and j < n):
        ar1[i], ar2[j] = ar2[j], ar1[i]
        i -= 1
        j += 1
 
    ar1.sort()
    ar2.sort()
 
    return (ar1[-1] + ar2[0]) >> 1
