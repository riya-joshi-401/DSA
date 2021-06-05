class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None 
        
        tmphead = head 
        nodemap = {}
        
        #first node for clone list
        tmpnode = Node(tmphead.val, None, None)
        newhead = tmpnode
        nodemap[tmphead] = tmpnode
        tmphead = tmphead.next
        while(tmphead):
            tmpnode = Node(tmphead.val, None, None)
            nodemap[tmphead] = tmpnode
            tmphead = tmphead.next 
            
        while (head):
            cur = nodemap[head]
            if (head.next != None):
                cur.next = nodemap[head.next]
            if (head.random != None):
                cur.random = nodemap[head.random]
            head = head.next 
            
        return newhead 
        
