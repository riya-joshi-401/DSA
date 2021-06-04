class Solution:
    def divide(self, N, head):
        even=[]
        odd=[]
        final=[]
        
        
        temp=head
        while temp:
            if temp.data%2==0:
                even.append(temp.data)
            else:
                odd.append(temp.data)
            temp=temp.next
         
        final=even+odd
        del even[:]
        del odd[:]
        
        ll = Linked_List()
        for i in final:
            ll.insert(i)
        
        return ll.head
