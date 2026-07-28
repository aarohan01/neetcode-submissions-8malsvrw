# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        ### Ancestor -> subtree should contain p and q or itself should be one  ###
        # Post order DFS 
        # Draw the 3 node diagram 
        # If we reach the end means root is

        
        def dfs(node):
            
            if not node :
               return None
                
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)


            if left and right:
                return node
                
            return left or right
        
        return dfs(root)