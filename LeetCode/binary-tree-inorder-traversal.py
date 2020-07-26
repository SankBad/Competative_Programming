# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        myarr = []
        self.CalcInorder(root, myarr)
        return myarr
        
        
        
    def CalcInorder(self, root, myarr):
        if root:
            self.CalcInorder(root.left, myarr)
            
            myarr.append(root.val)
            
            self.CalcInorder(root.right, myarr)
