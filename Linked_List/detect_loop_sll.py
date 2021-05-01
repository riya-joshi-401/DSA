
# Floyd’s Cycle-Finding Algorithm 
# Time complexity: O(n) , Space complexity: O(1)

"""
- Traverse linked list using two pointers.
- Move one pointer(slow_p) by one and another pointer(fast_p) by two.
- If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.

"""

class Solution:
    
    def detectLoop(self, head):
        
        fast = head
        slow = head
        while(slow != None and fast != None and fast.next!= None):
            slow = slow.next 
            fast = fast.next.next
            if(slow == fast):
                return True
       
        return False
      
      
  # https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
