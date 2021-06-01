class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        li=[]
        temp=head
        while temp: 
            li.append(temp.val)
            temp=temp.next
        temp=head
        li.sort()
        for i in li: 
            temp.val=i
            temp=temp.next
        return head
        
