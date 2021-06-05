class Solution:
    def splitList(self, head, head1, head2):
        
        head1=head
        temp=head
        n=0
        
        while temp:
            n+=1
            temp=temp.next
            if temp==head1:
                break
        i=1
        mid=n//2 - 1 if n%2==0 else n//2
        
        for i in range(n):
            
            if i==mid:
                head2=temp.next
                temp.next=head1
                break
            else:
                temp=temp.next
                
        ptr=head2
        
        for i in range(n-(n//2)):
            
            if ptr.next==head1:
                ptr.next=head2
                break
            else:
                ptr=ptr.next
            
        return head1,head2
