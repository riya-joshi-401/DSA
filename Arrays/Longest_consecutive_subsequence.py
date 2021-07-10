
# solution which i should follow







class Solution:
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, n):
        #using a Set to store elements.
        s = set(arr) 
        ans=0
     
        #checking each possible sequence from the start. 
        for i in range(n): 
      
            #if current element is starting element of a sequence then only 
            #we try to find out the length of sequence. 
            if (arr[i]-1) not in s: 
      
                j=arr[i] 
                #then we keep checking whether the next consecutive elements
                #are present in Set and we keep incrementing the counter. 
                while(j in s): 
                    j+=1
      
                #storing the maximum count.
                ans=max(ans, j-arr[i]) 
                
        #returning the length of longest subsequence.       
        return ans 
        
      

# MY SOL:-)
# acheived an execution time of 0.04 s IM SO PROUD OF MYSELF

class Solution:
    

    def findLongestConseqSubseq(self,arr, N):
        
        li=[]
        maxlen=0
        arr.sort()
        new=list(set(arr))
        
        
        for i in range(len(new)-1):
            
            if new[i+1]-new[i] ==1 and i<len(new)-3:
                li.append(new[i])
            elif new[i+1]-new[i] ==1 and i==len(new)-3:
                li.append(new[i])
                li.append(new[i+1])
            else:
                if 0<i<len(new)-2 and new[i]-new[i-1]==1 and new[i] not in li:
                    li.append(new[i])
                elif i==len(new)-2 and new[i+1]-new[i] ==1:
                    li.append(new[i+1])
                else:
                    pass
                if len(li)>maxlen:
                    maxlen=len(li)
                else:
                    pass
                li=[]
            
        return maxlen
