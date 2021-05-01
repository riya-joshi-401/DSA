def removeDuplicates(head):
    
    temp=head.next
    prev=head
    
    while temp:
        if prev.data==temp.data:
            prev.next=temp.next
            temp=prev.next 
        else:
            prev=temp
            temp=temp.next
            
