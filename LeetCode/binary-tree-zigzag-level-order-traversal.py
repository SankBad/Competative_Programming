# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]: 
        ans = []
        if root is None:
            return ans
        queue = []
        queue.append(root)
        left = True
        while(queue):
            currans = []
            length = len(queue)
            for i in range(length):
                currnode = queue.pop(0)
                currans.append(currnode.val)
                if currnode.left:
                    queue.append(currnode.left)
                if currnode.right:
                    queue.append(currnode.right)
            left = not left
            if left:
                currans.reverse()
            ans.append(currans)
        return ans
                
