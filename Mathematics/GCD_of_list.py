from functools import reduce
from fractions import gcd

arr=[2,3,60]
x=reduce(gcd,arr)
print(x)
#print(gcd(2,20))

# normally we also use import math and then math.gcd(2,20) but not for finding gcd for list
