class Node:

    def __init__ (self, data):
        self.data = data 
        self.next = None 
     
class LinkedList: 
 
    def __init__ (self):
        self.head = None 
      

    #insert at end    
    def insert_end(self,new_data):
        
        new_node=Node(new_data)
        
        if self.head==None: # if linked list is empty
            new_node.next=self.head
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
            new_node.next=None
            
    # display linked list
    def display(self): 
        
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
    # delete any element        
    def delete(self,val):
        
        if self.head==None:
            print("linked list is empty")
        else:
            temp=self.head
            # if the element to be deleted is the first element 
            if self.head.data==val:
                self.head=self.head.next
                x=temp.data
                temp=None
                x=None  
            else:
                while(temp.next.data!=val):
                    temp=temp.next
                    if temp.next==None:
                        print("val is not in linked list")
                        break
            
                if temp.next!=None:       
                    x=temp.next.data
                    temp.next=temp.next.next
                    x=None
                    
        
                

obj=LinkedList()    

obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)

obj.delete(10)

obj.display()
