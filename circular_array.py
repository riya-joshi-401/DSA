"""
This approach takes O(n) time and O(1) space.

"""

def prints(a, n, ind):
    
    i = ind
    # print from ind-th index to (n+i)th index.
    while i < n + ind :
        print(a[(i % n)], end = " ")
        i = i + 1
 

a = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(a);
prints(a, n, 3);
