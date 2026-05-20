# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        queue = deque()
        if root:
            queue.append(root)
        result = []
        while queue:
            res = 0

            for q in range(len(queue)):
                node = queue.popleft()
            
                res = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(res)        
        return result

        
        