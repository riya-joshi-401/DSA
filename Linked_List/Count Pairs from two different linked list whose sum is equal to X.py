class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        '''
        h1:  head of linkedList 1
        h2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:   len of linkedList 1
        X:   given sum
        '''
        count=0
        li=set()
        temp1=h1
        temp2=h2
        
        while temp1:
            li.add(temp1.data)
            temp1=temp1.next
            
        while temp2:
            if x-temp2.data in li:
                count+=1
            else:
                pass
            temp2=temp2.next
            
        
        return count
