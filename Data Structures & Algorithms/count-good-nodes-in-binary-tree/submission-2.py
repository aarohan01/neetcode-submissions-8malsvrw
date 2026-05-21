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
        #### Imp - note in obs - queue storing tuples to pass down max values to branches
        '''
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
        '''

        ##### DFS #####
        count = 0
        

        def dfs(node, maxval):
            nonlocal count
            if not node:
                return

            if node.val >= maxval:
                count += 1
                maxval = node.val
            
            dfs(node.left,maxval)
            dfs(node.right,maxval)
        
        dfs(root,root.val)
        return count

            
        

                