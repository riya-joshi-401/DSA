#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        
        temp1 = first
        temp2 = second
        
        li1 = []
        li2 = []
        
        while temp1:
            x = str(temp1.data)
            li1.append(x)
            temp1 = temp1.next
        while temp2:
            y = str(temp2.data)
            li2.append(y)
            temp2 = temp2.next
        n1 = ''.join(li1)
        n2 = ''.join(li2)
        n1 = int(n1)
        n2 = int(n2)
        summ = n1+n2
        summ = list(str(summ))
        ll = LinkedList()
        for i in summ:
            ll.insert(i)
        
        return ll.head
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends







------------------------------------------------------

def rev(head):
 curr, prev, next = head, None, None
 while curr: 
 next, curr.next = curr.next, prev
 prev, curr = curr, next
 return prev
 
def addLists(a, b):
 total = carry = 0
 one, two, node = rev(a), rev(b), Node(0)
 head = node
 while one or two or carry:
 d1, d2 = one.data if one else 0, two.data if two else 0
 total = d1 + d2 + carry
 carry = total // 10
 node.next = Node(total % 10)
 node = node.next
 one, two = one.next if one else None, two.next if two else None
 return rev(head.next)
