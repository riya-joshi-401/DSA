from collections import defaultdict

class Solution:
    def common_element(self,v1,v2):
        
        if v2==[]:
            v1.sort()
            return v1
        elif v1==[]:
            v2.sort()
            return v2
        else:
            ans=[]
            
            Map1 = defaultdict(lambda:0)
            Map2 = defaultdict(lambda:0)
            
            for i in v1:
                Map1[i]+=1
            for i in v2:
                Map2[i]+=1
        
            for i in Map1:
                if i in Map2:
                    
                    ans+=[i]*min(Map1[i],Map2[i])
                    
            ans.sort()        
            return ans
