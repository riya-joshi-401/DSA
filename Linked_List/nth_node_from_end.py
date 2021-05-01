def getNthFromLast(head,n):
    
    li=[]
    temp=head
    while temp:
        li.append(temp.data)
        temp=temp.next
    
    if len(li)<n:
        return -1
    else:
        return li[::-1][n-1]
