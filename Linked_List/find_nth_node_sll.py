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
            
    # find nth node        
    def find_nth_node(self,n):
        
        counter=0
        found=0
        temp=self.head
        while(temp):
            if counter==n-1:
                print("value of nth node is: ",temp.data)
                found=1
                break
            else:
                counter+=1
                temp=temp.next 
        if found==0:
            print("nth node not present :(")
                

obj=LinkedList()    

obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)


obj.display()

obj.find_nth_node(4)
