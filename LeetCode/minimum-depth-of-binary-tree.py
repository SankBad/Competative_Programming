# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        RootOrNot = self.isRoot(root)
        return self.FindMinDepth(root, RootOrNot)
        
        
    def FindMinDepth(self, root, RootOrNot):
        if root==None:
            if RootOrNot:
                return 0
            else:
                return float('inf')
        RootOrNot = self.isRoot(root)
        return min(1+self.FindMinDepth(root.left, RootOrNot), 1+self.FindMinDepth(root.right, RootOrNot))
    
    def isRoot(self, root):
        if root.left==root.right==None:
            return True
        else:
            return False
        
