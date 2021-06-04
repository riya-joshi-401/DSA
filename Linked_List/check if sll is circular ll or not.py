def isCircular(head):
    
    if head==None:
        return True
    else:
        temp=head
        while temp:
            temp=temp.next
            if temp==head:
                return True
                break
            
    return False
