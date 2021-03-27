
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
