
class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        
        curr, prev, next = head, None, None
        while curr: 
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        return prev


--------------------------------------------------------------------

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        
        prev = None
        curr = head
        ahead = head.next
        
        while curr is not None:
            ahead = curr.next       # Take the next node as ahead
            curr.next = prev        # Link current node to its previous
            prev = curr             # update prev as the current node
            curr = ahead            # update curr
        
        return prev
