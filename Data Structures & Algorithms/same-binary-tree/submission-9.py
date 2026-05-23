# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        '''
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
        '''

        ### Same logic different way of writing ###
        if not p and not q:
            return True
        
        if not p or not q:
            return False 
        
        if p and q and p.val != q.val:
            return False
        
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)

        return left and right



        ### BFS but exploring all nodes in both trees including nulls and then comparing ###
        """
        def bfs(root):
            queue = deque([root])
            array = []

            while queue:
                node = queue.popleft()

                if not node:
                    array.append(None)
                    continue

                array.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            return array        
        
        ## Same logic but writing my way / old way ##
        '''
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
        '''
        return bfs(q) == bfs(p)
        """




            