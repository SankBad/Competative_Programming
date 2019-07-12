# Python program to count node in loop linked list 
  
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
        # Function to insert a new  
    # node at the end  
    def AddNode(self, val): 
        if self.head is None: 
            self.head = Node(val) 
        else: 
            curr = self.head 
            while(curr.next): 
                curr = curr.next
            curr.next = Node(val) 
    
    def CreateLoop(self, n): 
          
        # LoopNode is the connecting node to 
        # the last node of linked list 
        LoopNode = self.head 
        for _ in range(1, n): 
            LoopNode = LoopNode.next
              
        # end is the last node of the Linked List 
        end = self.head 
        while(end.next): 
            end = end.next
              
        # Creating the loop 
        end.next = LoopNode 
    
    def countNodesinLoop(self):
        #Your code here
        slow = self.head
        fast = self.head
        count = 0
        temp = None
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow==fast):
                temp = slow
                break
        if temp is None:
            return(0)
        slow = temp
        fast = temp
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            count  = count + 1
            if (slow==fast):
                return(count)
        return(0)

            
# Setting up the code 
# Making a Linked List and adding the nodes 
myLL = LinkedList() 
myLL.AddNode(1) 
myLL.AddNode(2) 
myLL.AddNode(3) 
myLL.AddNode(4) 
myLL.AddNode(5) 
  
# Creating a loop in the linked List 
# Loop is created by connecting the  
# last node of linked list to n^th node 
# 1<= n <= len(LinkedList) 
myLL.CreateLoop(2) 
  
# Checking for Loop in the Linked List  
# and printing the length of the loop 
loopLength = myLL.countNodesinLoop() 
if myLL.head is None: 
    print("Linked list is empty") 
else: 
    print(str(loopLength)) 
