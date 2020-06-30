# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return self.CheckEqual(root.left, root.right)
        
    def CheckEqual(self, root1, root2):
        if root1==root2==None:
            return True
        elif root1==None and root2 != None:
            return False
        elif root2==None and root1 != None:
            return False
        elif root2.val != root1.val:
            return False
        return self.CheckEqual(root1.left, root2.right) and self.CheckEqual(root1.right, root2.left)
