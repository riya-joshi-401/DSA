def findMid(head):
    
    li=[]
    temp=head
    while temp:
        li.append(temp.data)
        temp=temp.next
        
    return li[len(li)//2]
    
# in case of even length was asked to find the second middle element

----------------------------------------------------------------------

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur=head
        l=0
        while(cur):
            l+=1
            cur=cur.next
        l=l//2
        while(l>0):
            head=head.next
            l-=1
        return head

