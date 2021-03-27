class Solution:
    def rearrange(self,arr, n):
        
        store_n=[]
        store_p=[]
        
        for i in arr:
            if i<0:
                store_n.append(i)
            else:
                store_p.append(i)
        if store_p and store_n:        
            del arr[::-1]
            
            if len(store_p)>len(store_n):
                maxi=store_p[1:]
                mini=store_n
            else:
                maxi=store_n
                mini=store_p[1:]
            
            arr.append(store_p[0])
            
            if maxi[0]>0:
                
                for i in range(len(maxi)):
                    
                    if i<len(mini):
                        arr.append(mini[i])
                    else:
                        pass
                    arr.append(maxi[i])
                    
            else:
                
                for i in range(len(maxi)):
                    
                    arr.append(maxi[i])
                    if i<len(mini):
                        arr.append(mini[i])
                
