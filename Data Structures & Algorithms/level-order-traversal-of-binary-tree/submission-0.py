# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        ### Idea of BFS ###
        # We want to visit each node, starting with root, store its children, then loop through 
        # the children, store theirs then same thing. Track level and values while doing this.
        # Since FIFO required for children we can use queue

        # Create a queue
        queue = deque()

        # Start with root node, if tree is not null
        if root:
            queue.append(root)

        # Storing the level and values
        level = 0
        result = []

        # Unless the queue is empty we loop through the queue, visit and append children
        while len(queue) > 0:
            res = []
            # Get children of all the nodes in queue and append & visit one by one node
            for i in range(len(queue)):
                curr = queue.popleft()
                res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            result.append(res)
            level += 1

        return result

            