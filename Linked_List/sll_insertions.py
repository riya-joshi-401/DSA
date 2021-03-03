
class Node: 
    
    def __init__(self, data): 
        self.data = data  
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
    # insert at beginning
    def insert_begin(self,new_data):
        
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

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
            
    # insert before
    def insert_before(self,before_data,new_data):
        
        if self.head==None: # if linked list is empty
            print("linked list is empty")
        
        else:
            temp=self.head
            
            if temp.data==before_data: # if elemented is to be inserted before first element
                new_node=Node(new_data)
                new_node.next=temp
                self.head=new_node
            
            else:
                while(temp.next.data!=before_data):
                    temp=temp.next
                if temp==None: # if the element before which is to be inserted is not present 
                    print("element not present in linked list")
                else:
                    new_node=Node(new_data)
                    new_node.next=temp.next
                    temp.next=new_node
    
    # insert after            
    def insert_after(self,after_data,new_data):
        
        if self.head==None:
            print("linked list is empty") # if linked list is empty
        else:
            temp=self.head
            
            while(temp.data!=after_data):
                temp=temp.next
            if temp==None:
                print("element not present in linked list")
            else:
                new_node=Node(new_data)
                new_node.next=temp.next
                temp.next=new_node
    
    # display linked list
    def display(self): 
        
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
            

obj=LinkedList()    

obj.insert_begin(40)
obj.insert_begin(30)
obj.insert_begin(20)
obj.insert_begin(10)

obj.insert_end(50)

obj.insert_before(20,15)
obj.insert_before(10,0)

obj.insert_after(50,60)
obj.insert_after(0,5)
obj.insert_after(30,35)

obj.display()
