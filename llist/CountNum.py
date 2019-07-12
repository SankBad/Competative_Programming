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
        
    def CountNum(self, num):
        print('abc')
        temp = self.head
        count1 = 0
        while(temp is not None):
            if temp.data == num:
                count1 = count1 + 1
            temp = temp.next
        return(count1)


llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1) 
  
# Check for the count function 
print (llist.CountNum(3))
