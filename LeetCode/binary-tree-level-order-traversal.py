# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        queue = []
        ans = []
        queue.append(root)
        while(queue):
            currlength = len(queue)
            currans = []
            for i in range(currlength):
                currnode = queue.pop(0)
                currans.append(currnode.val)
                if currnode.left is not None:
                    queue.append(currnode.left)
                if currnode.right is not None:
                    queue.append(currnode.right)
            ans.append(currans)
        return ans
            
