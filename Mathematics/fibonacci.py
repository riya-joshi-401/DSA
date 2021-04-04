# fibonacci  :  https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
# Fn = Fn-1 + Fn-2  with seed values : F0 = 0 and F1 = 1

# different methods to get the nth Fibonacci number

# (1) Using recursion
# time complexity: exponential , space complexity: O(n)

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
print(Fibonacci(9))

# (2) Dynamic Programming
# time and space : O(n)

def fibonacci(n):
     
    # Taking 1st two fibonacci nubers as 0 and 1
    f = [0, 1]
       
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(fibonacci(9))

# (3)Formula method
# time complexity: O(1) , space complexity: O(1)

import math
 
def fibo(n):
    phi = (1 + math.sqrt(5)) / 2
 
    return round(pow(phi, n) / math.sqrt(5))


