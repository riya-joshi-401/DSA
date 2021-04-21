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
            
    # display linked list
    def display(self): 
        
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
    # minimum and maximum   
    def min_max(self):
        
        minn=float('inf')
        maxx=float('-inf')
        temp=self.head
        
        while(temp):
            
            if temp.data>maxx:
                maxx=temp.data 
            if temp.data<minn:
                minn=temp.data

            temp=temp.next 
        
        print("max element: ",maxx) 
        print("min element: ",minn) 

obj=LinkedList()    

obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)


obj.display()

obj.min_max()
