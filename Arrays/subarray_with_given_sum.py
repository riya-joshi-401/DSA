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
