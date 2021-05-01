class Solution:
    
    def removeDuplicates(self, head):
        
        s=set()
        temp=head
        
        while temp.next is not None:
            s.add(temp.data)
            if temp.next.data in s:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
