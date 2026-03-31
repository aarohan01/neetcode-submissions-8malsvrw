# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:



        ### BFS ###
        ## Remember input is always in level order with null if any missing, and its binary tree not BST
        queue = deque()
        if root:
            queue.append(root)

        level = 0
        result = []

        while len(queue) > 0 :
            right = None
            for i in range(len(queue)):
                curr = queue.popleft()
                right = curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                
            result.append(right)
            level += 1
        return result

        