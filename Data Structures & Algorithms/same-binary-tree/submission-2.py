# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def bfs(node,array):

            queue = deque()
            queue.append(node)

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
            
            
        
        res1, res2 = [], []
        bfs(p,res1)
        bfs(q,res2)
        print(res1,res2)
        return res1 == res2

            


            