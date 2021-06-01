def multiplyTwoList(head1, head2):
        temp1 = head1
        temp2 = head2
        
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
        ans = n1*n2
        return ans%MOD
