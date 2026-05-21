# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        


        ### BFS ###
        
        maxval = root.val

        queue = deque()
        queue.append((root,maxval))

        count = 0
        level = 0

        while queue:

            for q in range(len(queue)):

                node, maxval = queue.popleft()
                if node.val >= maxval:
                    count += 1
                

                if node.left:
                    queue.append((node.left, max(maxval, node.val)))
                if node.right:
                    queue.append((node.right, max(maxval, node.val)))
            
            
            level += 1
        return count
                