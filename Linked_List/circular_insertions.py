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
            new_node.next=new_node # since it would be the first element so we will connect it with self (like a loop!!!!! :) )
            self.head=new_node
            
        else:
            
            new_node.next = self.head.next # connecting the new element to the first element
            self.head.next = new_node # connecting head to the new element
            self.head = new_node # making the head point to the new element
            
            
    # display linked list
    def display(self): 
        
        if self.head==None:
            print("Linked list is empty")
        else:
            temp=self.head.next # first element
            while True:
                print(temp.data)
                temp=temp.next
                if temp==self.head.next: # if again first element found stop :)
                    break
            
obj=LinkedList()    

obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)


obj.display()


################################################################################################################################################################################
class Node: 
    
    def __init__(self, data): 
        self.data = data  
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        

    # insert at begin
    def insert_end(self,new_data):
        
        new_node=Node(new_data)
        
        if self.head==None: # if linked list is empty
            new_node.next=new_node # since it would be the first element so we will connect it with self (like a loop!!!!! :) )
            self.head=new_node
            
        else:
            
            new_node.next = self.head # connecting the new element to the first element (front vala)
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node # connecting last element to new element
            self.head=new_node # makig the head point to the new element
            
            
    # display linked list
    def display(self): 
        
        if self.head==None:
            print("Linked list is empty")
        else:
            temp=self.head # first element
            while True:
                print(temp.data)
                temp=temp.next
                if temp==self.head: # if again first element found stop :)
                    break
            
obj=LinkedList()    

obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)


obj.display()


##############################################################################################################################################################################

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
            new_node.next=new_node # since it would be the first element so we will connect it with self (like a loop!!!!! :) )
            self.head=new_node
            
        else:
            
            new_node.next = self.head.next # connecting the new element to the first element
            self.head.next = new_node # connecting head to the new element
            self.head = new_node # making the head point to the new element
    
    # insert before
    def insert_before(self,before_data,new_data):
        
        if self.head==None: # if linked list is empty
            print("linked list is empty")
        
        else:
            temp=self.head.next
            
            if temp.data==before_data: # if elemented is to be inserted before first element
                new_node=Node(new_data)
                new_node.next=temp
                self.head.next=new_node
            
            else:
                while(temp.next.data!=before_data):
                    temp=temp.next
                    if temp==self.head: # if the element before which is to be inserted is not present 
                        print("element not present in linked list")
                        break
                if temp!=self.head:
                    new_node=Node(new_data)
                    new_node.next=temp.next
                    temp.next=new_node       
            
    # display linked list
    def display(self): 
        
        if self.head==None:
            print("Linked list is empty")
        else:
            temp=self.head.next # first element
            while True:
                print(temp.data)
                temp=temp.next
                if temp==self.head.next: # if again first element found stop :)
                    break
            
obj=LinkedList()    

obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)

obj.insert_before(20,15)
obj.insert_before(50,45)
obj.insert_before(10,0)
obj.insert_before(100,90)
obj.insert_before(50,49)
obj.insert_before(0,-1)

obj.display()

####################################################################################################################################################################


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
            new_node.next=new_node # since it would be the first element so we will connect it with self (like a loop!!!!! :) )
            self.head=new_node
            
        else:
            
            new_node.next = self.head.next # connecting the new element to the first element
            self.head.next = new_node # connecting head to the new element
            self.head = new_node # making the head point to the new element
    
  
    # insert after            
    def insert_after(self,after_data,new_data):
        
        counter=0
        
        if self.head==None:
            print("linked list is empty") # if linked list is empty
        else:
            temp=self.head
            
            while(temp.data!=after_data):
                temp=temp.next
                if temp==self.head:
                    counter+=1
                    break
                
            
            if counter==1: # if the element before which is to be inserted is not present 
                    print("element not present in linked list")
            else:

                new_node=Node(new_data)
                new_node.next=temp.next
                temp.next=new_node
                
                if after_data==self.head.data: # if element is to be inserted after the last element
                    self.head=new_node
            
    # display linked list
    def display(self): 
        
        if self.head==None:
            print("Linked list is empty")
        else:
            temp=self.head.next # first element
            while True:
                print(temp.data)
                temp=temp.next
                if temp==self.head.next: # if again first element found stop :)
                    break
            
obj=LinkedList()    

obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)

obj.insert_after(50,60)
obj.insert_after(0,5)
obj.insert_after(30,35)
obj.insert_after(10,15)

obj.display()
