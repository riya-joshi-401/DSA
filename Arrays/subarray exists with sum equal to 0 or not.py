

def subArrayExists(arr,n):
        
    s = set()

    sum = 0
    for i in range(n):
        sum += arr[i]
        print("sum",sum)
        
        #if prefix sum is 0 or if it is already present in set then it is
    		#repeated which means there is a subarray whose summation was 0,
    		#so we return true.
        if sum == 0 or sum in s:
            return True
            break
        s.add(sum)
        print("set",s)
        
    return False



arr = [4,2,-3,1,6]
 
print(subArrayExists(arr,5))
 
