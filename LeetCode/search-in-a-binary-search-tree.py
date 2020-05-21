class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None:
            return None
        if root.val<val:
            return self.searchBST(root.right,val)
        elif root.val>val:
            return self.searchBST(root.left,val)
        else:
            return root
            
