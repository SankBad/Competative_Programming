# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def SearchInt(self, root: 'TreeNode', p: 'TreeNode'):
        if root==None:
            return False
        if root.val == p:
            return True
        lefexist = self.SearchInt(root.left, p)
        if lefexist:
            return True
        rightexist = self.SearchInt(root.right, p)
        return rightexist
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        First = ((self.SearchInt(root.left, p.val))&(self.SearchInt(root.left, q.val)))
        Second = ((self.SearchInt(root.right, p.val))&(self.SearchInt(root.right, q.val)))
        if ((First==False) & (Second==False)):
            return root
        elif (First==True):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (Second==True):
            return self.lowestCommonAncestor(root.right, p, q)'''

### another solution

class Solution:
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        if root==p or root==q:
            return root
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        if leftLCA and rightLCA:
            return root
        if rightLCA==None:
            return leftLCA
        else:
            return rightLCA
            
            
            
        
        
            
            
        
        
