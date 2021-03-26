"""
def subArraySum(A, n, x): 
    
    for i in range(n):
      temp=0
      j=i
      
      while (temp <x) and (j<n):
          temp=temp+A[j]
          if temp==x:
              return [i+1,j+1]
              
          j+=1
    return [-1]
"""

def subArrayExists(arr,n):
        
    s = set()

    sum = 0
    for i in range(n):
        sum += arr[i]
        print("sum",sum)
        
        if sum == 0 or sum in s:
            return True
            break
        s.add(sum)
        print("set",s)
        
    return False



arr = [4,2,-3,1,6]
 
print(subArrayExists(arr,5))
 
