# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        RootOrNot = self.isRoot(root)
        return self.CalcSum(root, 0, sum, RootOrNot)
    
    def isRoot(self, root):
        if root.left==root.right==None:
            return True
        else:
            return False
        
    def CalcSum(self, root, currsum, sum, RootOrNot):
        if root==None:
            if (currsum==sum and RootOrNot):
                return True
            else:
                return False            
        currsum = root.val + currsum
        RootOrNot = self.isRoot(root)
        return (self.CalcSum(root.left, currsum, sum, RootOrNot)) or (self.CalcSum(root.right, currsum, sum, RootOrNot)) 
        
        
