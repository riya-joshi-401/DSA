
class Node: 
    
    def __init__(self, data): 
        self.data = data  
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        

    # insert at end    
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
    
    # delete begin    
    def delete_begin(self):
        
        if self.head==None:
            print("linked list is empty")
        else:
            temp=self.head
            self.head=self.head.next
            x=temp.data
            temp=None
            x=None
    
    # delete end    
    def delete_end(self):
        
        if self.head==None:
            print("linked list is empty")
        else:
            temp=self.head
            if self.head.next==None: # if only one element is there in the element
                self.head=self.head.next
                x=temp.data
                temp=None
                x=None
            else:
                while(temp.next.next!=None):
                    temp=temp.next
                x=temp.next.data
                temp.next=None
                x=None
    
    # delete before        
    def delete_before(self,before_data):
        
        if self.head==None:
            print("linked list is empty")
        elif self.head.data==before_data:
            print("this is the first element no element before it to delete :)")
        else:
            temp=self.head
            
            if temp.next.data==before_data:
                self.head=self.head.next
                x=temp.data
                temp=None
                x=None 
            
            else:
                while(temp.next.next.data!=before_data):
                    temp=temp.next
                    if temp.next.next==None:
                        print("before_data is not in linked list")
                        break
                if temp.next!=None:
                    x=temp.next.data
                    temp.next=temp.next.next
                    x=None
                
    
    # delete after
    def delete_after(self,after_data):
        if self.head==None:
            print("linked list is empty")
        elif self.head.next==None:
            print("this is the only element no element after it to delete :)")
        else:
            temp=self.head
            
            while(temp.data!=after_data):
                temp=temp.next
                if temp.next==None:
                    print("after_data is not in linked list")
                    break
            
            if temp.next!=None:       
                x=temp.next.data
                temp.next=temp.next.next
                x=None
            
    # display linked list
    def display(self): 
        
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            

obj=LinkedList()    


obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)


obj.delete_begin()

obj.delete_end()

obj.delete_before(100)
obj.delete_before(30)
obj.delete_before(40)

obj.delete_after(100)
obj.delete_after(30)

obj.display()
