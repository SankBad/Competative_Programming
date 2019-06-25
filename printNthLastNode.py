# Print N th last node from end
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
        
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        
    def printNthLastNode(self, n):
        temp = self.head
        length = 0
        while(temp is not None):
            temp =  temp.next
            length = length + 1

        if (length<n):
            print('not possible')

        temp = self.head

        for i in range(0, length-n):
            temp = temp.next
        print(temp.data)
    
        
# Driver Code         
llist = LinkedList()  
llist.push(20)  
llist.push(4)  
llist.push(15)  
llist.push(35) 
llist.printNthLastNode(4) 
