# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def bfs(node):

            queue = deque()
            queue.append(node)

            array = []
            while queue:
                
                node = queue.popleft()
                if node :
                    array.append(node.val)
                else:
                    array.append(None)

                if node :
                    
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(None)

                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(None)

            return array
        
        return bfs(q) == bfs(p)

            


            