# Python program to detect loop in the linked list 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    
    def detectLoop(self):
        #code here
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow =  slow.next
            fast = fast.next.next
            if(slow==fast):
                print('True')
                return
        print('False')
        return

            
# Driver program for testing 
llist = LinkedList()
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
  
# Create a loop for testing 
llist.head.next.next.next.next = llist.head 
llist.detectLoop() 
