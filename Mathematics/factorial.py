# using in-built method
import math

num = int(input("Enter the number to find factorial: "))
fact = math.factorial(num) # works for only integral values

# using iterative method

fact = 1
if num<0:
  print("factorial doesn't exists")
elif num==0:
  fact=1
else:
  for i in range(1, num+1):
      fact = fact*i
      
# using recursive method

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
  
# for finding factorial for non-integral values

math.gamma(num-1)
# https://stackoverflow.com/questions/10056797/python-calculate-factorial-of-a-non-integral-number
