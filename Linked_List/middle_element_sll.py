def findMid(head):
    
    li=[]
    temp=head
    while temp:
        li.append(temp.data)
        temp=temp.next
        
    return li[len(li)//2]
    
