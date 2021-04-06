from fractions import gcd

def lcm(a,b):
    return a*b / gcd(a,b)
 
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))
