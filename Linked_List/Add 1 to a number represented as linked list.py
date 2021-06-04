class Solution:
    def addOne(self,head):
        
        s=''
        temp=head
        
        while temp:
            s+=str(temp.data)
            temp=temp.next
            
        s=int(s)
        s=s+1
        li=list(map(int, str(s)))
        
        ll = LinkedList()
        for i in li:
            ll.insert(i)
        
        return ll.head
