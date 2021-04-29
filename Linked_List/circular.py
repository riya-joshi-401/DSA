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
