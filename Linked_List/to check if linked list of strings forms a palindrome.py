def compute(head): 
    
    li=[]
    temp=head
    while temp:
        li.append(temp.data)
        temp=temp.next
        
    if li[:]==li[::-1]:
        return True
    else:
        return False
