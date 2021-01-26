# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        while(queue):
            length = len(queue)
            for i in range(length):
                currnode = queue.popleft()
                if currnode.left:
                    queue.append(currnode.left)
                if currnode.right:
                    queue.append(currnode.right)
            ans.append(currnode.val)
        return ans
