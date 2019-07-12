class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None

def ConstructBST(arr):
    
    if not arr:
        return
    
    mid = int(len(arr)/2)
    
    root = Node(arr[mid])
    
    root.left = ConstructBST(arr[0:mid])
    root.right = ConstructBST(arr[mid+1:])
    
    return root

def InOrder(root):
    if root == None:
        return
    InOrder(root.left)
    print(root.data, end = ' ')
    InOrder(root.right) 


arr = [1, 3, 5, 8, 7, 6, 2, 4, 9, 13, 14, 11, 12]
arr.sort()
root = ConstructBST(arr)
InOrder(root)
